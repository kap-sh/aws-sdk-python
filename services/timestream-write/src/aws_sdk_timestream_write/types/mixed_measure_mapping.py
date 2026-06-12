"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MixedMeasureMapping``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.measure_value_type
    import aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list
    import aws_sdk_timestream_write.types.schema_name


class MixedMeasureMapping(TypedDict):
    measure_name: NotRequired["aws_sdk_timestream_write.types.schema_name.SchemaName"]
    """<p></p>"""
    source_column: NotRequired["aws_sdk_timestream_write.types.schema_name.SchemaName"]
    """<p></p>"""
    target_measure_name: NotRequired[
        "aws_sdk_timestream_write.types.schema_name.SchemaName"
    ]
    """<p></p>"""
    measure_value_type: (
        "aws_sdk_timestream_write.types.measure_value_type.MeasureValueType"
    )
    """<p></p>"""
    multi_measure_attribute_mappings: NotRequired[
        "aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list.MultiMeasureAttributeMappingList"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MixedMeasureMapping) -> dict:
    out: dict = {}
    if "measure_name" in value:
        out["MeasureName"] = value["measure_name"]
    if "source_column" in value:
        out["SourceColumn"] = value["source_column"]
    if "target_measure_name" in value:
        out["TargetMeasureName"] = value["target_measure_name"]
    import aws_sdk_timestream_write.types.measure_value_type

    out["MeasureValueType"] = (
        aws_sdk_timestream_write.types.measure_value_type.serialize_aws_json_1_0(
            value["measure_value_type"]
        )
    )
    if "multi_measure_attribute_mappings" in value:
        import aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list

        out["MultiMeasureAttributeMappings"] = (
            aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list.serialize_aws_json_1_0(
                value["multi_measure_attribute_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MixedMeasureMapping:
    out: MixedMeasureMapping = {}  # type: ignore[typeddict-item]
    if "MeasureName" in data:
        out["measure_name"] = data["MeasureName"]
    if "SourceColumn" in data:
        out["source_column"] = data["SourceColumn"]
    if "TargetMeasureName" in data:
        out["target_measure_name"] = data["TargetMeasureName"]
    if "MeasureValueType" in data:
        import aws_sdk_timestream_write.types.measure_value_type

        out["measure_value_type"] = (
            aws_sdk_timestream_write.types.measure_value_type.deserialize_aws_json_1_0(
                data["MeasureValueType"]
            )
        )
    else:
        raise DeserializationError("MixedMeasureMapping.measure_value_type required")
    if "MultiMeasureAttributeMappings" in data:
        import aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list

        out["multi_measure_attribute_mappings"] = (
            aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list.deserialize_aws_json_1_0(
                data["MultiMeasureAttributeMappings"]
            )
        )
    return out
