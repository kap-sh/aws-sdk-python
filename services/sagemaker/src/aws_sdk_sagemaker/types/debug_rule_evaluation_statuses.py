"""Generated from Smithy shape ``com.amazonaws.sagemaker#DebugRuleEvaluationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.debug_rule_evaluation_status

DebugRuleEvaluationStatuses: TypeAlias = list[
    "aws_sdk_sagemaker.types.debug_rule_evaluation_status.DebugRuleEvaluationStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DebugRuleEvaluationStatuses) -> list:
    import aws_sdk_sagemaker.types.debug_rule_evaluation_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.debug_rule_evaluation_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DebugRuleEvaluationStatuses:
    import aws_sdk_sagemaker.types.debug_rule_evaluation_status

    out: DebugRuleEvaluationStatuses = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.debug_rule_evaluation_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
