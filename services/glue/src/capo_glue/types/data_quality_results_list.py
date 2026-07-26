"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.data_quality_result

DataQualityResultsList: TypeAlias = list[
    "capo_glue.types.data_quality_result.DataQualityResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultsList) -> list:
    import capo_glue.types.data_quality_result

    out: list = []
    for item in value:
        out.append(capo_glue.types.data_quality_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityResultsList:
    import capo_glue.types.data_quality_result

    out: DataQualityResultsList = []
    for item in data:
        out.append(capo_glue.types.data_quality_result.deserialize_aws_json_1_1(item))
    return out
