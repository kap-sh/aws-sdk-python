"""Generated from Smithy shape ``com.amazonaws.appstream#ListAssociatedFleetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string


class ListAssociatedFleetsRequest(TypedDict, closed=True):
    stack_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the stack.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssociatedFleetsRequest) -> dict:
    out: dict = {}
    if "stack_name" in value:
        out["StackName"] = value["stack_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssociatedFleetsRequest:
    out: ListAssociatedFleetsRequest = {}  # type: ignore[typeddict-item]
    if "StackName" in data:
        out["stack_name"] = data["StackName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
