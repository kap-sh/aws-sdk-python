"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetSchemaMappingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name


class GetSchemaMappingInput(TypedDict, closed=True):
    schema_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaMappingInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSchemaMappingInput:
    out: GetSchemaMappingInput = {}  # type: ignore[typeddict-item]
    return out
