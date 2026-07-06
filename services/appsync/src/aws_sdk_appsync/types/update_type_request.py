"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.resource_name
    import aws_sdk_appsync.types.string
    import aws_sdk_appsync.types.type_definition_format


class UpdateTypeRequest(TypedDict, closed=True):
    api_id: "aws_sdk_appsync.types.string.String"
    """<p>The API ID.</p>"""
    type_name: "aws_sdk_appsync.types.resource_name.ResourceName"
    """<p>The new type name.</p>"""
    definition: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The new definition.</p>"""
    format: "aws_sdk_appsync.types.type_definition_format.TypeDefinitionFormat"
    """<p>The new type format: SDL or JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTypeRequest) -> dict:
    out: dict = {}
    if "definition" in value:
        out["definition"] = value["definition"]
    import aws_sdk_appsync.types.type_definition_format

    out["format"] = aws_sdk_appsync.types.type_definition_format.serialize_json(
        value["format"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTypeRequest:
    out: UpdateTypeRequest = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        out["definition"] = data["definition"]
    if "format" in data:
        import aws_sdk_appsync.types.type_definition_format

        out["format"] = aws_sdk_appsync.types.type_definition_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("UpdateTypeRequest.format required")
    return out
