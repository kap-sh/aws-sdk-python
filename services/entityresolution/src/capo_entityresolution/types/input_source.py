"""Generated from Smithy shape ``com.amazonaws.entityresolution#InputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.entity_name
    import capo_entityresolution.types.input_source_arn


class InputSource(TypedDict, closed=True):
    input_source_arn: "capo_entityresolution.types.input_source_arn.InputSourceARN"
    """<p>An Glue table Amazon Resource Name (ARN) for the input source table.</p>"""
    schema_name: "capo_entityresolution.types.entity_name.EntityName"
    """<p>The name of the schema to be retrieved.</p>"""
    apply_normalization: NotRequired["bool"]
    """<p>Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an <code>AttributeType</code> of <code>PHONE_NUMBER</code>, and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSource) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    out["schemaName"] = value["schema_name"]
    if "apply_normalization" in value:
        out["applyNormalization"] = value["apply_normalization"]
    return out


def deserialize_json(data: dict) -> InputSource:
    out: InputSource = {}  # type: ignore[typeddict-item]
    if "inputSourceARN" in data:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        raise DeserializationError("InputSource.input_source_arn required")
    if "schemaName" in data:
        out["schema_name"] = data["schemaName"]
    else:
        raise DeserializationError("InputSource.schema_name required")
    if "applyNormalization" in data:
        out["apply_normalization"] = data["applyNormalization"]
    return out
