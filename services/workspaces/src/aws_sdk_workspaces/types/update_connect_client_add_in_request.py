"""Generated from Smithy shape ``com.amazonaws.workspaces#UpdateConnectClientAddInRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.add_in_name
    import aws_sdk_workspaces.types.add_in_url
    import aws_sdk_workspaces.types.amazon_uuid
    import aws_sdk_workspaces.types.directory_id


class UpdateConnectClientAddInRequest(TypedDict):
    add_in_id: "aws_sdk_workspaces.types.amazon_uuid.AmazonUuid"
    """<p>The identifier of the client add-in to update.</p>"""
    resource_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier for which the client add-in is configured.</p>"""
    name: NotRequired["aws_sdk_workspaces.types.add_in_name.AddInName"]
    """<p>The name of the client add-in.</p>"""
    url: NotRequired["aws_sdk_workspaces.types.add_in_url.AddInUrl"]
    """<p>The endpoint URL of the Connect Customer client add-in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectClientAddInRequest) -> dict:
    out: dict = {}
    out["AddInId"] = value["add_in_id"]
    out["ResourceId"] = value["resource_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "url" in value:
        out["URL"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectClientAddInRequest:
    out: UpdateConnectClientAddInRequest = {}  # type: ignore[typeddict-item]
    if "AddInId" in data:
        out["add_in_id"] = data["AddInId"]
    else:
        raise DeserializationError("UpdateConnectClientAddInRequest.add_in_id required")
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "UpdateConnectClientAddInRequest.resource_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "URL" in data:
        out["url"] = data["URL"]
    return out
