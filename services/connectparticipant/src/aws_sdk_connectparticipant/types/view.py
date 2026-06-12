"""Generated from Smithy shape ``com.amazonaws.connectparticipant#View``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.arn
    import aws_sdk_connectparticipant.types.view_content
    import aws_sdk_connectparticipant.types.view_id
    import aws_sdk_connectparticipant.types.view_name
    import aws_sdk_connectparticipant.types.view_version


class View(TypedDict):
    id: NotRequired["aws_sdk_connectparticipant.types.view_id.ViewId"]
    """<p>The identifier of the view.</p>"""
    arn: NotRequired["aws_sdk_connectparticipant.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view.</p>"""
    name: NotRequired["aws_sdk_connectparticipant.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    version: NotRequired["aws_sdk_connectparticipant.types.view_version.ViewVersion"]
    """<p>The current version of the view.</p>"""
    content: NotRequired["aws_sdk_connectparticipant.types.view_content.ViewContent"]
    """<p>View content containing all content necessary to render a view except for runtime input data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: View) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "content" in value:
        import aws_sdk_connectparticipant.types.view_content

        out["Content"] = aws_sdk_connectparticipant.types.view_content.serialize_json(
            value["content"]
        )
    return out


def deserialize_json(data: dict) -> View:
    out: View = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Content" in data:
        import aws_sdk_connectparticipant.types.view_content

        out["content"] = aws_sdk_connectparticipant.types.view_content.deserialize_json(
            data["Content"]
        )
    return out
