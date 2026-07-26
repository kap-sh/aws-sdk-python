"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityObservations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_observation

DataQualityObservations: TypeAlias = list[
    "capo_glue.types.data_quality_observation.DataQualityObservation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityObservations) -> list:
    import capo_glue.types.data_quality_observation

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.data_quality_observation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityObservations:
    import capo_glue.types.data_quality_observation

    out: DataQualityObservations = []
    for item in data:
        out.append(
            capo_glue.types.data_quality_observation.deserialize_aws_json_1_1(item)
        )
    return out
