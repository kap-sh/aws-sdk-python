"""Generated from Smithy shape ``com.amazonaws.oam#CreateSinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_oam.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_oam.types.sink_name
    import aws_sdk_oam.types.tag_map_input


class CreateSinkInput(TypedDict, closed=True):
    name: "aws_sdk_oam.types.sink_name.SinkName"
    """<p>A name for the sink.</p>"""
    tags: NotRequired["aws_sdk_oam.types.tag_map_input.TagMapInput"]
    r"""<p>Assigns one or more tags (key-value pairs) to the link. </p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>For more information about using tags to control access, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html\">Controlling access to Amazon Web Services resources using tags</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSinkInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_oam.types.tag_map_input

        out["Tags"] = aws_sdk_oam.types.tag_map_input.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSinkInput:
    out: CreateSinkInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSinkInput.name required")
    if "Tags" in data:
        import aws_sdk_oam.types.tag_map_input

        out["tags"] = aws_sdk_oam.types.tag_map_input.deserialize_json(data["Tags"])
    return out
