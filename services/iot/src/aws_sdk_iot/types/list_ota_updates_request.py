"""Generated from Smithy shape ``com.amazonaws.iot#ListOTAUpdatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.max_results
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.ota_update_status


class ListOTAUpdatesRequest(TypedDict):
    max_results: NotRequired["aws_sdk_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token used to retrieve the next set of results.</p>"""
    ota_update_status: NotRequired[
        "aws_sdk_iot.types.ota_update_status.OTAUpdateStatus"
    ]
    """<p>The OTA update job status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOTAUpdatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOTAUpdatesRequest:
    out: ListOTAUpdatesRequest = {}  # type: ignore[typeddict-item]
    return out
