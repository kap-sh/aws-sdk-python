"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_rule_result

DataQualityRuleResults: TypeAlias = list[
    "aws_sdk_glue.types.data_quality_rule_result.DataQualityRuleResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleResults) -> list:
    import aws_sdk_glue.types.data_quality_rule_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.data_quality_rule_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DataQualityRuleResults:
    import aws_sdk_glue.types.data_quality_rule_result

    out: DataQualityRuleResults = []
    for item in data:
        out.append(
            aws_sdk_glue.types.data_quality_rule_result.deserialize_aws_json_1_1(item)
        )
    return out
