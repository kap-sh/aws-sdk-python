"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackRuleEvaluationResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_evaluation_result

ConformancePackRuleEvaluationResultsList: TypeAlias = list[
    "capo_config_service.types.conformance_pack_evaluation_result.ConformancePackEvaluationResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackRuleEvaluationResultsList) -> list:
    import capo_config_service.types.conformance_pack_evaluation_result

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.conformance_pack_evaluation_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConformancePackRuleEvaluationResultsList:
    import capo_config_service.types.conformance_pack_evaluation_result

    out: ConformancePackRuleEvaluationResultsList = []
    for item in data:
        out.append(
            capo_config_service.types.conformance_pack_evaluation_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
