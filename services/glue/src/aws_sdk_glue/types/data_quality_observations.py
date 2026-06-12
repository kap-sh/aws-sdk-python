"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityObservations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_observation

DataQualityObservations: TypeAlias = list[
    "aws_sdk_glue.types.data_quality_observation.DataQualityObservation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityObservations) -> list:
    import aws_sdk_glue.types.data_quality_observation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.data_quality_observation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityObservations:
    import aws_sdk_glue.types.data_quality_observation

    out: DataQualityObservations = []
    for item in data:
        out.append(
            aws_sdk_glue.types.data_quality_observation.deserialize_aws_json_1_1(item)
        )
    return out
