"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MultiMeasureMappings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list
    import aws_sdk_timestream_write.types.schema_name


class MultiMeasureMappings(TypedDict):
    target_multi_measure_name: NotRequired[
        "aws_sdk_timestream_write.types.schema_name.SchemaName"
    ]
    """<p></p>"""
    multi_measure_attribute_mappings: "aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list.MultiMeasureAttributeMappingList"
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultiMeasureMappings) -> dict:
    out: dict = {}
    if "target_multi_measure_name" in value:
        out["TargetMultiMeasureName"] = value["target_multi_measure_name"]
    import aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list

    out["MultiMeasureAttributeMappings"] = (
        aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list.serialize_aws_json_1_0(
            value["multi_measure_attribute_mappings"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MultiMeasureMappings:
    out: MultiMeasureMappings = {}  # type: ignore[typeddict-item]
    if "TargetMultiMeasureName" in data:
        out["target_multi_measure_name"] = data["TargetMultiMeasureName"]
    if "MultiMeasureAttributeMappings" in data:
        import aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list

        out["multi_measure_attribute_mappings"] = (
            aws_sdk_timestream_write.types.multi_measure_attribute_mapping_list.deserialize_aws_json_1_0(
                data["MultiMeasureAttributeMappings"]
            )
        )
    else:
        raise DeserializationError(
            "MultiMeasureMappings.multi_measure_attribute_mappings required"
        )
    return out
