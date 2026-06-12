"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MultiMeasureAttributeMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.scalar_measure_value_type
    import aws_sdk_timestream_write.types.schema_name


class MultiMeasureAttributeMapping(TypedDict):
    source_column: "aws_sdk_timestream_write.types.schema_name.SchemaName"
    """<p></p>"""
    target_multi_measure_attribute_name: NotRequired[
        "aws_sdk_timestream_write.types.schema_name.SchemaName"
    ]
    """<p></p>"""
    measure_value_type: NotRequired[
        "aws_sdk_timestream_write.types.scalar_measure_value_type.ScalarMeasureValueType"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultiMeasureAttributeMapping) -> dict:
    out: dict = {}
    out["SourceColumn"] = value["source_column"]
    if "target_multi_measure_attribute_name" in value:
        out["TargetMultiMeasureAttributeName"] = value[
            "target_multi_measure_attribute_name"
        ]
    if "measure_value_type" in value:
        import aws_sdk_timestream_write.types.scalar_measure_value_type

        out["MeasureValueType"] = (
            aws_sdk_timestream_write.types.scalar_measure_value_type.serialize_aws_json_1_0(
                value["measure_value_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MultiMeasureAttributeMapping:
    out: MultiMeasureAttributeMapping = {}  # type: ignore[typeddict-item]
    if "SourceColumn" in data:
        out["source_column"] = data["SourceColumn"]
    else:
        raise DeserializationError(
            "MultiMeasureAttributeMapping.source_column required"
        )
    if "TargetMultiMeasureAttributeName" in data:
        out["target_multi_measure_attribute_name"] = data[
            "TargetMultiMeasureAttributeName"
        ]
    if "MeasureValueType" in data:
        import aws_sdk_timestream_write.types.scalar_measure_value_type

        out["measure_value_type"] = (
            aws_sdk_timestream_write.types.scalar_measure_value_type.deserialize_aws_json_1_0(
                data["MeasureValueType"]
            )
        )
    return out
