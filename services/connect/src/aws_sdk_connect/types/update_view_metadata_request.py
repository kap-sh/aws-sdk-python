"""Generated from Smithy shape ``com.amazonaws.connect#UpdateViewMetadataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.view_description
    import aws_sdk_connect.types.view_id
    import aws_sdk_connect.types.view_name
    import aws_sdk_connect.types.views_instance_id


class UpdateViewMetadataRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.views_instance_id.ViewsInstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    view_id: "aws_sdk_connect.types.view_id.ViewId"
    """<p>The identifier of the view. Both <code>ViewArn</code> and <code>ViewId</code> can be used.</p>"""
    name: NotRequired["aws_sdk_connect.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    description: NotRequired["aws_sdk_connect.types.view_description.ViewDescription"]
    """<p>The description of the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateViewMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateViewMetadataRequest:
    out: UpdateViewMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
