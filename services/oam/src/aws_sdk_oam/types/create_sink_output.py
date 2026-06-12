"""Generated from Smithy shape ``com.amazonaws.oam#CreateSinkOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_oam.types.tag_map_output


class CreateSinkOutput(TypedDict):
    arn: NotRequired["str"]
    """<p>The ARN of the sink that is newly created.</p>"""
    id: NotRequired["str"]
    """<p>The random ID string that Amazon Web Services generated as part of the sink ARN.</p>"""
    name: NotRequired["str"]
    """<p>The name of the sink.</p>"""
    tags: NotRequired["aws_sdk_oam.types.tag_map_output.TagMapOutput"]
    """<p>The tags assigned to the sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSinkOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "tags" in value:
        import aws_sdk_oam.types.tag_map_output

        out["Tags"] = aws_sdk_oam.types.tag_map_output.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSinkOutput:
    out: CreateSinkOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Tags" in data:
        import aws_sdk_oam.types.tag_map_output

        out["tags"] = aws_sdk_oam.types.tag_map_output.deserialize_json(data["Tags"])
    return out
