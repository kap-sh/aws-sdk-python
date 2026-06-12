"""Generated from Smithy shape ``com.amazonaws.pipes#MultiMeasureAttributeMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.measure_value
    import aws_sdk_pipes.types.measure_value_type
    import aws_sdk_pipes.types.multi_measure_attribute_name


class MultiMeasureAttributeMapping(TypedDict):
    measure_value: "aws_sdk_pipes.types.measure_value.MeasureValue"
    """<p>Dynamic path to the measurement attribute in the source event.</p>"""
    measure_value_type: "aws_sdk_pipes.types.measure_value_type.MeasureValueType"
    """<p>Data type of the measurement attribute in the source event.</p>"""
    multi_measure_attribute_name: (
        "aws_sdk_pipes.types.multi_measure_attribute_name.MultiMeasureAttributeName"
    )
    """<p>Target measure name to be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiMeasureAttributeMapping) -> dict:
    out: dict = {}
    out["MeasureValue"] = value["measure_value"]
    out["MeasureValueType"] = value["measure_value_type"]
    out["MultiMeasureAttributeName"] = value["multi_measure_attribute_name"]
    return out


def deserialize_json(data: dict) -> MultiMeasureAttributeMapping:
    out: MultiMeasureAttributeMapping = {}  # type: ignore[typeddict-item]
    if "MeasureValue" in data:
        out["measure_value"] = data["MeasureValue"]
    else:
        raise DeserializationError(
            "MultiMeasureAttributeMapping.measure_value required"
        )
    if "MeasureValueType" in data:
        out["measure_value_type"] = data["MeasureValueType"]
    else:
        raise DeserializationError(
            "MultiMeasureAttributeMapping.measure_value_type required"
        )
    if "MultiMeasureAttributeName" in data:
        out["multi_measure_attribute_name"] = data["MultiMeasureAttributeName"]
    else:
        raise DeserializationError(
            "MultiMeasureAttributeMapping.multi_measure_attribute_name required"
        )
    return out
