"""Generated from Smithy shape ``com.amazonaws.timestreamquery#MixedMeasureMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.mixed_measure_mapping

MixedMeasureMappingList: TypeAlias = list[
    "aws_sdk_timestream_query.types.mixed_measure_mapping.MixedMeasureMapping"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MixedMeasureMappingList) -> list:
    import aws_sdk_timestream_query.types.mixed_measure_mapping

    out: list = []
    for item in value:
        out.append(
            aws_sdk_timestream_query.types.mixed_measure_mapping.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MixedMeasureMappingList:
    import aws_sdk_timestream_query.types.mixed_measure_mapping

    out: MixedMeasureMappingList = []
    for item in data:
        out.append(
            aws_sdk_timestream_query.types.mixed_measure_mapping.deserialize_aws_json_1_0(
                item
            )
        )
    return out
