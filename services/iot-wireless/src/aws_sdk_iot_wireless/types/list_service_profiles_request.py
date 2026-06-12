"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListServiceProfilesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.max_results
    import aws_sdk_iot_wireless.types.next_token


class ListServiceProfilesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>To retrieve the next set of results, the <code>nextToken</code> value from a previous response; otherwise <b>null</b> to receive the first set of results.</p>"""
    max_results: "aws_sdk_iot_wireless.types.max_results.MaxResults"
    """<p>The maximum number of results to return in this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServiceProfilesRequest:
    out: ListServiceProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
