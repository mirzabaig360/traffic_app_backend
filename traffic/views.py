from django.core.paginator import Paginator, EmptyPage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer


@api_view(['GET'])
def day_of_week_average_count(request):
    # Get the start_date and end_date from the query parameters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Validate that start_date and end_date are present in the query parameters
    if not start_date or not end_date:
        return Response({'error': "Both start_date and end_date query parameters are required."},
                        status=status.HTTP_400_BAD_REQUEST)

    # Retrieve the SensorData instances from the database that fall within the specified date range
    data = SensorData.objects.filter(date__gte=start_date, date__lte=end_date)

    # Check if there is any data within the specified date range
    if not data.exists():
        return Response({'error': "No data found within the specified date range."},
                        status=status.HTTP_404_NOT_FOUND)

    # Get the current page number from the query parameters (default to page 1)
    page_number = request.GET.get('page', 1)

    # Set the number of items to display per page (you can change this as needed)
    items_per_page = 10

    # Use Django's Paginator to paginate the queryset
    paginator = Paginator(data, items_per_page)

    try:
        # Get the current page from the paginator
        current_page = paginator.page(page_number)
    except EmptyPage:
        return Response({'error': "Page not found."}, status=status.HTTP_404_NOT_FOUND)

    # Serialize the data for the current page using the SensorDataSerializer
    serializer = SensorDataSerializer(current_page, many=True)

    # Return the paginated data as the response
    return Response({
        'count': paginator.count,
        'next': current_page.next_page_number() if current_page.has_next() else None,
        'previous': current_page.previous_page_number() if current_page.has_previous() else None,
        'results': serializer.data
    })
