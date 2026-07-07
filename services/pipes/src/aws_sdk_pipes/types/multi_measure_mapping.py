"""Generated from Smithy shape ``com.amazonaws.pipes#MultiMeasureMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.multi_measure_attribute_mappings
    import aws_sdk_pipes.types.multi_measure_name


class MultiMeasureMapping(TypedDict, closed=True):
    multi_measure_name: "aws_sdk_pipes.types.multi_measure_name.MultiMeasureName"
    """<p>The name of the multiple measurements per record (multi-measure).</p>"""
    multi_measure_attribute_mappings: "aws_sdk_pipes.types.multi_measure_attribute_mappings.MultiMeasureAttributeMappings"
    """<p>Mappings that represent multiple source event fields mapped to measures in the same Timestream for LiveAnalytics record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiMeasureMapping) -> dict:
    out: dict = {}
    out["MultiMeasureName"] = value["multi_measure_name"]
    import aws_sdk_pipes.types.multi_measure_attribute_mappings

    out["MultiMeasureAttributeMappings"] = (
        aws_sdk_pipes.types.multi_measure_attribute_mappings.serialize_json(
            value["multi_measure_attribute_mappings"]
        )
    )
    return out


def deserialize_json(data: dict) -> MultiMeasureMapping:
    out: MultiMeasureMapping = {}  # type: ignore[typeddict-item]
    if "MultiMeasureName" in data:
        out["multi_measure_name"] = data["MultiMeasureName"]
    else:
        raise DeserializationError("MultiMeasureMapping.multi_measure_name required")
    if "MultiMeasureAttributeMappings" in data:
        import aws_sdk_pipes.types.multi_measure_attribute_mappings

        out["multi_measure_attribute_mappings"] = (
            aws_sdk_pipes.types.multi_measure_attribute_mappings.deserialize_json(
                data["MultiMeasureAttributeMappings"]
            )
        )
    else:
        raise DeserializationError(
            "MultiMeasureMapping.multi_measure_attribute_mappings required"
        )
    return out
