"""Generated from Smithy shape ``com.amazonaws.m2#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.entity_name_list
    import aws_sdk_m2.types.identifier
    import aws_sdk_m2.types.max_results
    import aws_sdk_m2.types.next_token


class ListApplicationsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_m2.types.next_token.NextToken"]
    """<p>A pagination token to control the number of applications displayed in the list.</p>"""
    max_results: NotRequired["aws_sdk_m2.types.max_results.MaxResults"]
    """<p>The maximum number of applications to return.</p>"""
    names: NotRequired["aws_sdk_m2.types.entity_name_list.EntityNameList"]
    """<p>The names of the applications.</p>"""
    environment_id: NotRequired["aws_sdk_m2.types.identifier.Identifier"]
    """<p>The unique identifier of the runtime environment where the applications are deployed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
