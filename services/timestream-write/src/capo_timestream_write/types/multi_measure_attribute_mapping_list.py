"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MultiMeasureAttributeMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_timestream_write.types.multi_measure_attribute_mapping

MultiMeasureAttributeMappingList: TypeAlias = list[
    "capo_timestream_write.types.multi_measure_attribute_mapping.MultiMeasureAttributeMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MultiMeasureAttributeMappingList) -> list:
    import capo_timestream_write.types.multi_measure_attribute_mapping

    out: list = []
    for item in value:
        out.append(
            capo_timestream_write.types.multi_measure_attribute_mapping.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MultiMeasureAttributeMappingList:
    import capo_timestream_write.types.multi_measure_attribute_mapping

    out: MultiMeasureAttributeMappingList = []
    for item in data:
        out.append(
            capo_timestream_write.types.multi_measure_attribute_mapping.deserialize_aws_json_1_0(
                item
            )
        )
    return out
