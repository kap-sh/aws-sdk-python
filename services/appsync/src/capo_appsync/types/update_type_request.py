"""Generated from Smithy shape ``com.amazonaws.appsync#UpdateTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appsync.types.resource_name
    import capo_appsync.types.string
    import capo_appsync.types.type_definition_format


class UpdateTypeRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""
    type_name: "capo_appsync.types.resource_name.ResourceName"
    """<p>The new type name.</p>"""
    definition: NotRequired["capo_appsync.types.string.String"]
    """<p>The new definition.</p>"""
    format: "capo_appsync.types.type_definition_format.TypeDefinitionFormat"
    """<p>The new type format: SDL or JSON.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTypeRequest) -> dict:
    out: dict = {}
    if "definition" in value:
        out["definition"] = value["definition"]
    import capo_appsync.types.type_definition_format

    out["format"] = capo_appsync.types.type_definition_format.serialize_json(
        value["format"]
    )
    return out


def deserialize_json(data: dict) -> UpdateTypeRequest:
    out: UpdateTypeRequest = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        out["definition"] = data["definition"]
    if "format" in data:
        import capo_appsync.types.type_definition_format

        out["format"] = capo_appsync.types.type_definition_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("UpdateTypeRequest.format required")
    return out
