"""Generated from Smithy shape ``com.amazonaws.workspaces#ConnectClientAddIn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.add_in_name
    import aws_sdk_workspaces.types.add_in_url
    import aws_sdk_workspaces.types.amazon_uuid
    import aws_sdk_workspaces.types.directory_id


class ConnectClientAddIn(TypedDict, closed=True):
    add_in_id: NotRequired["aws_sdk_workspaces.types.amazon_uuid.AmazonUuid"]
    """<p>The client add-in identifier.</p>"""
    resource_id: NotRequired["aws_sdk_workspaces.types.directory_id.DirectoryId"]
    """<p>The directory identifier for which the client add-in is configured.</p>"""
    name: NotRequired["aws_sdk_workspaces.types.add_in_name.AddInName"]
    """<p>The name of the client add in.</p>"""
    url: NotRequired["aws_sdk_workspaces.types.add_in_url.AddInUrl"]
    """<p>The endpoint URL of the client add-in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectClientAddIn) -> dict:
    out: dict = {}
    if "add_in_id" in value:
        out["AddInId"] = value["add_in_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "url" in value:
        out["URL"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectClientAddIn:
    out: ConnectClientAddIn = {}  # type: ignore[typeddict-item]
    if "AddInId" in data:
        out["add_in_id"] = data["AddInId"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "URL" in data:
        out["url"] = data["URL"]
    return out
