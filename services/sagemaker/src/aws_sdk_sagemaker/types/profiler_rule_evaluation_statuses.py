"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProfilerRuleEvaluationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.profiler_rule_evaluation_status

ProfilerRuleEvaluationStatuses: TypeAlias = list[
    "aws_sdk_sagemaker.types.profiler_rule_evaluation_status.ProfilerRuleEvaluationStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilerRuleEvaluationStatuses) -> list:
    import aws_sdk_sagemaker.types.profiler_rule_evaluation_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.profiler_rule_evaluation_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProfilerRuleEvaluationStatuses:
    import aws_sdk_sagemaker.types.profiler_rule_evaluation_status

    out: ProfilerRuleEvaluationStatuses = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.profiler_rule_evaluation_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
