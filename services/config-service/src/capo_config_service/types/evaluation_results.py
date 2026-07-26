"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.evaluation_result

EvaluationResults: TypeAlias = list[
    "capo_config_service.types.evaluation_result.EvaluationResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationResults) -> list:
    import capo_config_service.types.evaluation_result

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.evaluation_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EvaluationResults:
    import capo_config_service.types.evaluation_result

    out: EvaluationResults = []
    for item in data:
        out.append(
            capo_config_service.types.evaluation_result.deserialize_aws_json_1_1(item)
        )
    return out
