"""Generated from Smithy shape ``com.amazonaws.configservice#AggregateEvaluationResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.aggregate_evaluation_result

AggregateEvaluationResultList: TypeAlias = list[
    "capo_config_service.types.aggregate_evaluation_result.AggregateEvaluationResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregateEvaluationResultList) -> list:
    import capo_config_service.types.aggregate_evaluation_result

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.aggregate_evaluation_result.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AggregateEvaluationResultList:
    import capo_config_service.types.aggregate_evaluation_result

    out: AggregateEvaluationResultList = []
    for item in data:
        out.append(
            capo_config_service.types.aggregate_evaluation_result.deserialize_aws_json_1_1(
                item
            )
        )
    return out
