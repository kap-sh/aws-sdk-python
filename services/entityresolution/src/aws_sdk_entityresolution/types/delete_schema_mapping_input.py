"""Generated from Smithy shape ``com.amazonaws.entityresolution#DeleteSchemaMappingInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name


class DeleteSchemaMappingInput(TypedDict):
    schema_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSchemaMappingInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSchemaMappingInput:
    out: DeleteSchemaMappingInput = {}  # type: ignore[typeddict-item]
    return out
