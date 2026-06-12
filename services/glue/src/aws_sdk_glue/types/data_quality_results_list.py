"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_result

DataQualityResultsList: TypeAlias = list[
    "aws_sdk_glue.types.data_quality_result.DataQualityResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityResultsList) -> list:
    import aws_sdk_glue.types.data_quality_result

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.data_quality_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityResultsList:
    import aws_sdk_glue.types.data_quality_result

    out: DataQualityResultsList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.data_quality_result.deserialize_aws_json_1_1(item)
        )
    return out
