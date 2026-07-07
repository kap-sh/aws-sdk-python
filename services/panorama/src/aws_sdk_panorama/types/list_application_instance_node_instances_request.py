"""Generated from Smithy shape ``com.amazonaws.panorama#ListApplicationInstanceNodeInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.application_instance_id
    import aws_sdk_panorama.types.max_size25
    import aws_sdk_panorama.types.next_token


class ListApplicationInstanceNodeInstancesRequest(TypedDict, closed=True):
    application_instance_id: (
        "aws_sdk_panorama.types.application_instance_id.ApplicationInstanceId"
    )
    """<p>The node instances' application instance ID.</p>"""
    max_results: "aws_sdk_panorama.types.max_size25.MaxSize25"
    """<p>The maximum number of node instances to return in one page of results.</p>"""
    next_token: NotRequired["aws_sdk_panorama.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationInstanceNodeInstancesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationInstanceNodeInstancesRequest:
    out: ListApplicationInstanceNodeInstancesRequest = {}  # type: ignore[typeddict-item]
    return out
