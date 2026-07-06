"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListRegionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.next_token
    import aws_sdk_workspaces_instances.types.region_list


class ListRegionsResponse(TypedDict, closed=True):
    regions: "aws_sdk_workspaces_instances.types.region_list.RegionList"
    """<p>Collection of AWS regions supported by WorkSpaces Instances.</p>"""
    next_token: NotRequired["aws_sdk_workspaces_instances.types.next_token.NextToken"]
    """<p>Token for retrieving additional regions if the result set is paginated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRegionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_instances.types.region_list

    out["Regions"] = (
        aws_sdk_workspaces_instances.types.region_list.serialize_aws_json_1_0(
            value["regions"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRegionsResponse:
    out: ListRegionsResponse = {}  # type: ignore[typeddict-item]
    if "Regions" in data:
        import aws_sdk_workspaces_instances.types.region_list

        out["regions"] = (
            aws_sdk_workspaces_instances.types.region_list.deserialize_aws_json_1_0(
                data["Regions"]
            )
        )
    else:
        raise DeserializationError("ListRegionsResponse.regions required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
