"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetMatchIdInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.entity_name
    import aws_sdk_entityresolution.types.record_attribute_map


class GetMatchIdInput(TypedDict):
    workflow_name: "aws_sdk_entityresolution.types.entity_name.EntityName"
    """<p>The name of the workflow.</p>"""
    record: "aws_sdk_entityresolution.types.record_attribute_map.RecordAttributeMap"
    """<p>The record to fetch the Match ID for.</p>"""
    apply_normalization: "bool"
    """<p>Normalizes the attributes defined in the schema in the input data. For example, if an attribute has an <code>AttributeType</code> of <code>PHONE_NUMBER</code>, and the data in the input table is in a format of 1234567890, Entity Resolution will normalize this field in the output to (123)-456-7890.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMatchIdInput) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.record_attribute_map

    out["record"] = aws_sdk_entityresolution.types.record_attribute_map.serialize_json(
        value["record"]
    )
    out["applyNormalization"] = value.get("apply_normalization", True)
    return out


def deserialize_json(data: dict) -> GetMatchIdInput:
    out: GetMatchIdInput = {}  # type: ignore[typeddict-item]
    if "record" in data:
        import aws_sdk_entityresolution.types.record_attribute_map

        out["record"] = (
            aws_sdk_entityresolution.types.record_attribute_map.deserialize_json(
                data["record"]
            )
        )
    else:
        raise DeserializationError("GetMatchIdInput.record required")
    if "applyNormalization" in data:
        out["apply_normalization"] = data["applyNormalization"]
    else:
        out["apply_normalization"] = True
    return out
