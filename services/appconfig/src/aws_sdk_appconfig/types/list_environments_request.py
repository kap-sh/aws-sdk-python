"""Generated from Smithy shape ``com.amazonaws.appconfig#ListEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.max_results
    import aws_sdk_appconfig.types.next_token


class ListEnvironmentsRequest(TypedDict, closed=True):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    max_results: NotRequired["aws_sdk_appconfig.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["aws_sdk_appconfig.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentsRequest:
    out: ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    return out
