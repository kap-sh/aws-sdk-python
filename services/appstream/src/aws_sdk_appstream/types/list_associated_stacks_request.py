"""Generated from Smithy shape ``com.amazonaws.appstream#ListAssociatedStacksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string


class ListAssociatedStacksRequest(TypedDict):
    fleet_name: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The name of the fleet.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If this value is null, it retrieves the first page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssociatedStacksRequest) -> dict:
    out: dict = {}
    if "fleet_name" in value:
        out["FleetName"] = value["fleet_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssociatedStacksRequest:
    out: ListAssociatedStacksRequest = {}  # type: ignore[typeddict-item]
    if "FleetName" in data:
        out["fleet_name"] = data["FleetName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
