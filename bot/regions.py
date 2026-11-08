"""Internal routing adapter for one AZIYA park. No region choice or fallback."""
from bot.route_settings import destination

PARK = 'aziya'


def get_region(context):
    return PARK


def region_name(region):
    return 'AZIYA TAXI'


def clear_application(context):
    context.user_data.clear()


def driver_groups(region=PARK):
    if region != PARK:
        return []
    return [value for key in ('DRIVER_GROUP_1', 'DRIVER_GROUP_2')
            if (value := destination(key))]


def application_group(region, kind):
    return destination('BRAND_GROUP') if region == PARK and kind == 'brand' else ''


def archive_group(region=PARK):
    return destination('ARCHIVE_GROUP') if region == PARK else ''
