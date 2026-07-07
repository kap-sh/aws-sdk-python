"""Generated from Smithy shape ``com.amazonaws.panorama#ListApplicationInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device_id
    import aws_sdk_panorama.types.max_size25
    import aws_sdk_panorama.types.next_token
    import aws_sdk_panorama.types.status_filter


class ListApplicationInstancesRequest(TypedDict, closed=True):
    device_id: NotRequired["aws_sdk_panorama.types.device_id.DeviceId"]
    """<p>The application instances' device ID.</p>"""
    status_filter: NotRequired["aws_sdk_panorama.types.status_filter.StatusFilter"]
    """<p>Only include instances with a specific status.</p>"""
    max_results: "aws_sdk_panorama.types.max_size25.MaxSize25"
    """<p>The maximum number of application instances to return in one page of results.</p>"""
    next_token: NotRequired["aws_sdk_panorama.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationInstancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationInstancesRequest:
    out: ListApplicationInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
