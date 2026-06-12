"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityAnalyzerResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_analyzer_result

DataQualityAnalyzerResults: TypeAlias = list[
    "aws_sdk_glue.types.data_quality_analyzer_result.DataQualityAnalyzerResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityAnalyzerResults) -> list:
    import aws_sdk_glue.types.data_quality_analyzer_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.data_quality_analyzer_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityAnalyzerResults:
    import aws_sdk_glue.types.data_quality_analyzer_result

    out: DataQualityAnalyzerResults = []
    for item in data:
        out.append(
            aws_sdk_glue.types.data_quality_analyzer_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
