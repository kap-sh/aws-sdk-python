"""Generated from Smithy shape ``com.amazonaws.m2#ListApplicationVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.max_results
    import aws_sdk_m2.types.next_token


class ListApplicationVersionsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.</p>"""
    max_results: NotRequired["aws_sdk_m2.types.max_results.MaxResults"]
    """<p>The maximum number of application versions to return.</p>"""
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationVersionsRequest:
    out: ListApplicationVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
