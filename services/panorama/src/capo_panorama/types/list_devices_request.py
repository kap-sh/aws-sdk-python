"""Generated from Smithy shape ``com.amazonaws.panorama#ListDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.device_aggregated_status
    import capo_panorama.types.list_devices_sort_by
    import capo_panorama.types.max_size25
    import capo_panorama.types.name_filter
    import capo_panorama.types.next_token
    import capo_panorama.types.sort_order


class ListDevicesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: "capo_panorama.types.max_size25.MaxSize25"
    """<p>The maximum number of devices to return in one page of results.</p>"""
    sort_by: NotRequired["capo_panorama.types.list_devices_sort_by.ListDevicesSortBy"]
    """<p>The target column to be sorted on. Default column sort is CREATED_TIME.</p>"""
    sort_order: NotRequired["capo_panorama.types.sort_order.SortOrder"]
    """<p>The sorting order for the returned list. SortOrder is DESCENDING by default based on CREATED_TIME. Otherwise, SortOrder is ASCENDING.</p>"""
    name_filter: NotRequired["capo_panorama.types.name_filter.NameFilter"]
    """<p>Filter based on device's name. Prefixes supported.</p>"""
    device_aggregated_status_filter: NotRequired[
        "capo_panorama.types.device_aggregated_status.DeviceAggregatedStatus"
    ]
    """<p>Filter based on a device's status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDevicesRequest:
    out: ListDevicesRequest = {}  # type: ignore[typeddict-item]
    return out
