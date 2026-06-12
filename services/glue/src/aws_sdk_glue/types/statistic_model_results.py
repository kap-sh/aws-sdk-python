"""Generated from Smithy shape ``com.amazonaws.glue#StatisticModelResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.statistic_model_result

StatisticModelResults: TypeAlias = list[
    "aws_sdk_glue.types.statistic_model_result.StatisticModelResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatisticModelResults) -> list:
    import aws_sdk_glue.types.statistic_model_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.statistic_model_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StatisticModelResults:
    import aws_sdk_glue.types.statistic_model_result

    out: StatisticModelResults = []
    for item in data:
        out.append(
            aws_sdk_glue.types.statistic_model_result.deserialize_aws_json_1_1(item)
        )
    return out
