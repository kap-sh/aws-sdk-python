"""Generated from Smithy shape ``com.amazonaws.appsync#Type``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string
    import aws_sdk_appsync.types.type_definition_format


class Type(TypedDict):
    name: NotRequired["aws_sdk_appsync.types.resource_name.ResourceName"]
    """<p>The type name.</p>"""
    description: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The type description.</p>"""
    arn: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The type Amazon Resource Name (ARN).</p>"""
    definition: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The type definition.</p>"""
    format: NotRequired[
        "aws_sdk_appsync.types.type_definition_format.TypeDefinitionFormat"
    ]
    """<p>The type format: SDL or JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Type) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "definition" in value:
        out["definition"] = value["definition"]
    if "format" in value:
        import aws_sdk_appsync.types.type_definition_format

        out["format"] = aws_sdk_appsync.types.type_definition_format.serialize_json(
            value["format"]
        )
    return out


def deserialize_json(data: dict) -> Type:
    out: Type = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "definition" in data:
        out["definition"] = data["definition"]
    if "format" in data:
        import aws_sdk_appsync.types.type_definition_format

        out["format"] = aws_sdk_appsync.types.type_definition_format.deserialize_json(
            data["format"]
        )
    return out
