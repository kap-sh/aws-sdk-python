"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceEvaluations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.resource_evaluation

ResourceEvaluations: TypeAlias = list[
    "capo_config_service.types.resource_evaluation.ResourceEvaluation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceEvaluations) -> list:
    import capo_config_service.types.resource_evaluation

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.resource_evaluation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceEvaluations:
    import capo_config_service.types.resource_evaluation

    out: ResourceEvaluations = []
    for item in data:
        out.append(
            capo_config_service.types.resource_evaluation.deserialize_aws_json_1_1(item)
        )
    return out
