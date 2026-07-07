"""Generated from Smithy shape ``com.amazonaws.schemas#CreateSchemaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__string
    import aws_sdk_schemas.types.__string_min0_max256
    import aws_sdk_schemas.types.__string_min1_max100000
    import aws_sdk_schemas.types.tags
    import aws_sdk_schemas.types.type


class CreateSchemaRequest(TypedDict, closed=True):
    content: NotRequired[
        "aws_sdk_schemas.types.__string_min1_max100000.__stringMin1Max100000"
    ]
    """<p>The source of the schema definition.</p>"""
    description: NotRequired[
        "aws_sdk_schemas.types.__string_min0_max256.__stringMin0Max256"
    ]
    """<p>A description of the schema.</p>"""
    registry_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the registry.</p>"""
    schema_name: "aws_sdk_schemas.types.__string.__string"
    """<p>The name of the schema.</p>"""
    tags: NotRequired["aws_sdk_schemas.types.tags.Tags"]
    """<p>Tags associated with the schema.</p>"""
    type: NotRequired["aws_sdk_schemas.types.type.Type"]
    """<p>The type of schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSchemaRequest) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.serialize_json(value["tags"])
    if "type" in value:
        import aws_sdk_schemas.types.type

        out["Type"] = aws_sdk_schemas.types.type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> CreateSchemaRequest:
    out: CreateSchemaRequest = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "tags" in data:
        import aws_sdk_schemas.types.tags

        out["tags"] = aws_sdk_schemas.types.tags.deserialize_json(data["tags"])
    if "Type" in data:
        import aws_sdk_schemas.types.type

        out["type"] = aws_sdk_schemas.types.type.deserialize_json(data["Type"])
    return out
