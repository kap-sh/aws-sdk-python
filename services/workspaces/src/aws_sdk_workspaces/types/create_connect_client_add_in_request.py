"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateConnectClientAddInRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.add_in_name
    import aws_sdk_workspaces.types.add_in_url
    import aws_sdk_workspaces.types.directory_id


class CreateConnectClientAddInRequest(TypedDict):
    resource_id: "aws_sdk_workspaces.types.directory_id.DirectoryId"
    """<p>The directory identifier for which to configure the client add-in.</p>"""
    name: "aws_sdk_workspaces.types.add_in_name.AddInName"
    """<p>The name of the client add-in.</p>"""
    url: "aws_sdk_workspaces.types.add_in_url.AddInUrl"
    """<p>The endpoint URL of the Connect Customer client add-in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectClientAddInRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    out["Name"] = value["name"]
    out["URL"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectClientAddInRequest:
    out: CreateConnectClientAddInRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError(
            "CreateConnectClientAddInRequest.resource_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateConnectClientAddInRequest.name required")
    if "URL" in data:
        out["url"] = data["URL"]
    else:
        raise DeserializationError("CreateConnectClientAddInRequest.url required")
    return out
