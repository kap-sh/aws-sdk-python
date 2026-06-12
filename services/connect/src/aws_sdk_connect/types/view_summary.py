"""Generated from Smithy shape ``com.amazonaws.connect#ViewSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.view_description
    import aws_sdk_connect.types.view_id
    import aws_sdk_connect.types.view_name
    import aws_sdk_connect.types.view_status
    import aws_sdk_connect.types.view_type


class ViewSummary(TypedDict):
    id: NotRequired["aws_sdk_connect.types.view_id.ViewId"]
    """<p>The identifier of the view.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view.</p>"""
    name: NotRequired["aws_sdk_connect.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    type: NotRequired["aws_sdk_connect.types.view_type.ViewType"]
    """<p>The type of the view.</p>"""
    status: NotRequired["aws_sdk_connect.types.view_status.ViewStatus"]
    """<p>Indicates the view status as either <code>SAVED</code> or <code>PUBLISHED</code>. The <code>PUBLISHED</code> status will initiate validation on the content.</p>"""
    description: NotRequired["aws_sdk_connect.types.view_description.ViewDescription"]
    """<p>The description of the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_connect.types.view_type

        out["Type"] = aws_sdk_connect.types.view_type.serialize_json(value["type"])
    if "status" in value:
        import aws_sdk_connect.types.view_status

        out["Status"] = aws_sdk_connect.types.view_status.serialize_json(
            value["status"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ViewSummary:
    out: ViewSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_connect.types.view_type

        out["type"] = aws_sdk_connect.types.view_type.deserialize_json(data["Type"])
    if "Status" in data:
        import aws_sdk_connect.types.view_status

        out["status"] = aws_sdk_connect.types.view_status.deserialize_json(
            data["Status"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
