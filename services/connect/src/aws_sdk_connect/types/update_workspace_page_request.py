"""Generated from Smithy shape ``com.amazonaws.connect#UpdateWorkspacePageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.input_data
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.page
    import aws_sdk_connect.types.slug
    import aws_sdk_connect.types.workspace_id


class UpdateWorkspacePageRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "aws_sdk_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    page: "aws_sdk_connect.types.page.Page"
    """<p>The current page identifier.</p>"""
    new_page: NotRequired["aws_sdk_connect.types.page.Page"]
    """<p>The new page identifier, if changing the page name.</p>"""
    resource_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view to associate with the page.</p>"""
    slug: NotRequired["aws_sdk_connect.types.slug.Slug"]
    """<p>The URL-friendly identifier for the page.</p>"""
    input_data: NotRequired["aws_sdk_connect.types.input_data.InputData"]
    """<p>A JSON string containing input parameters for the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspacePageRequest) -> dict:
    out: dict = {}
    if "new_page" in value:
        out["NewPage"] = value["new_page"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "slug" in value:
        out["Slug"] = value["slug"]
    if "input_data" in value:
        out["InputData"] = value["input_data"]
    return out


def deserialize_json(data: dict) -> UpdateWorkspacePageRequest:
    out: UpdateWorkspacePageRequest = {}  # type: ignore[typeddict-item]
    if "NewPage" in data:
        out["new_page"] = data["NewPage"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Slug" in data:
        out["slug"] = data["Slug"]
    if "InputData" in data:
        out["input_data"] = data["InputData"]
    return out
