"""Generated from Smithy shape ``com.amazonaws.pipes#SingleMeasureMapping``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.measure_name
    import aws_sdk_pipes.types.measure_value
    import aws_sdk_pipes.types.measure_value_type


class SingleMeasureMapping(TypedDict):
    measure_value: "aws_sdk_pipes.types.measure_value.MeasureValue"
    """<p>Dynamic path of the source field to map to the measure in the record.</p>"""
    measure_value_type: "aws_sdk_pipes.types.measure_value_type.MeasureValueType"
    """<p>Data type of the source field.</p>"""
    measure_name: "aws_sdk_pipes.types.measure_name.MeasureName"
    """<p>Target measure name for the measurement attribute in the Timestream table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingleMeasureMapping) -> dict:
    out: dict = {}
    out["MeasureValue"] = value["measure_value"]
    out["MeasureValueType"] = value["measure_value_type"]
    out["MeasureName"] = value["measure_name"]
    return out


def deserialize_json(data: dict) -> SingleMeasureMapping:
    out: SingleMeasureMapping = {}  # type: ignore[typeddict-item]
    if "MeasureValue" in data:
        out["measure_value"] = data["MeasureValue"]
    else:
        raise DeserializationError("SingleMeasureMapping.measure_value required")
    if "MeasureValueType" in data:
        out["measure_value_type"] = data["MeasureValueType"]
    else:
        raise DeserializationError("SingleMeasureMapping.measure_value_type required")
    if "MeasureName" in data:
        out["measure_name"] = data["MeasureName"]
    else:
        raise DeserializationError("SingleMeasureMapping.measure_name required")
    return out
