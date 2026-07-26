"""Generated from Smithy shape ``com.amazonaws.entityresolution#Record``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import capo_entityresolution.types.input_source_arn
    import capo_entityresolution.types.record_attribute_map_string255
    import capo_entityresolution.types.unique_id


class Record(TypedDict, closed=True):
    input_source_arn: "capo_entityresolution.types.input_source_arn.InputSourceARN"
    """<p> The input source ARN of the record.</p>"""
    unique_id: "capo_entityresolution.types.unique_id.UniqueId"
    """<p> The unique ID of the record.</p>"""
    record_attribute_map: "capo_entityresolution.types.record_attribute_map_string255.RecordAttributeMapString255"
    """<p> The record's attribute map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Record) -> dict:
    out: dict = {}
    out["inputSourceARN"] = value["input_source_arn"]
    out["uniqueId"] = value["unique_id"]
    import capo_entityresolution.types.record_attribute_map_string255

    out["recordAttributeMap"] = (
        capo_entityresolution.types.record_attribute_map_string255.serialize_json(
            value["record_attribute_map"]
        )
    )
    return out


def deserialize_json(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if "inputSourceARN" in data:
        out["input_source_arn"] = data["inputSourceARN"]
    else:
        raise DeserializationError("Record.input_source_arn required")
    if "uniqueId" in data:
        out["unique_id"] = data["uniqueId"]
    else:
        raise DeserializationError("Record.unique_id required")
    if "recordAttributeMap" in data:
        import capo_entityresolution.types.record_attribute_map_string255

        out["record_attribute_map"] = (
            capo_entityresolution.types.record_attribute_map_string255.deserialize_json(
                data["recordAttributeMap"]
            )
        )
    else:
        raise DeserializationError("Record.record_attribute_map required")
    return out
