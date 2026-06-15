"""Generated from Smithy shape ``com.amazonaws.connect#CreateWorkspacePageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.input_data
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.page
    import aws_sdk_connect.types.slug
    import aws_sdk_connect.types.workspace_id


class CreateWorkspacePageRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "aws_sdk_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    resource_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the view to associate with the page.</p>"""
    page: "aws_sdk_connect.types.page.Page"
    """<p>The page identifier. Valid system pages include <code>HOME</code> and <code>AGENT_EXPERIENCE</code>. Custom pages cannot use the <code>aws:</code> or <code>connect:</code> prefixes.</p>"""
    slug: NotRequired["aws_sdk_connect.types.slug.Slug"]
    """<p>The URL-friendly identifier for the page.</p>"""
    input_data: NotRequired["aws_sdk_connect.types.input_data.InputData"]
    """<p>A JSON string containing input parameters for the view, validated against the view's input schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspacePageRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["Page"] = value["page"]
    if "slug" in value:
        out["Slug"] = value["slug"]
    if "input_data" in value:
        out["InputData"] = value["input_data"]
    return out


def deserialize_json(data: dict) -> CreateWorkspacePageRequest:
    out: CreateWorkspacePageRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("CreateWorkspacePageRequest.resource_arn required")
    if "Page" in data:
        out["page"] = data["Page"]
    else:
        raise DeserializationError("CreateWorkspacePageRequest.page required")
    if "Slug" in data:
        out["slug"] = data["Slug"]
    if "InputData" in data:
        out["input_data"] = data["InputData"]
    return out
