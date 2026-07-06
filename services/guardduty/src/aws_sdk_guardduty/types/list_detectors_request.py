"""Generated from Smithy shape ``com.amazonaws.guardduty#ListDetectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.max_results
    import aws_sdk_guardduty.types.string


class ListDetectorsRequest(TypedDict, closed=True):
    max_results: NotRequired["aws_sdk_guardduty.types.max_results.MaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items that you want in the response. The default value is 50. The maximum value is 50.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDetectorsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDetectorsRequest:
    out: ListDetectorsRequest = {}  # type: ignore[typeddict-item]
    return out
