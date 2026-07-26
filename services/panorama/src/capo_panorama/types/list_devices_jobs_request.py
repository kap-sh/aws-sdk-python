"""Generated from Smithy shape ``com.amazonaws.panorama#ListDevicesJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.device_id
    import capo_panorama.types.max_size25
    import capo_panorama.types.next_token


class ListDevicesJobsRequest(TypedDict, closed=True):
    device_id: NotRequired["capo_panorama.types.device_id.DeviceId"]
    """<p>Filter results by the job's target device ID.</p>"""
    next_token: NotRequired["capo_panorama.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: "capo_panorama.types.max_size25.MaxSize25"
    """<p>The maximum number of device jobs to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDevicesJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDevicesJobsRequest:
    out: ListDevicesJobsRequest = {}  # type: ignore[typeddict-item]
    return out
