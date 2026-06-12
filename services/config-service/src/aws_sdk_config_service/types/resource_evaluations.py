"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceEvaluations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.resource_evaluation

ResourceEvaluations: TypeAlias = list[
    "aws_sdk_config_service.types.resource_evaluation.ResourceEvaluation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceEvaluations) -> list:
    import aws_sdk_config_service.types.resource_evaluation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.resource_evaluation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceEvaluations:
    import aws_sdk_config_service.types.resource_evaluation

    out: ResourceEvaluations = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.resource_evaluation.deserialize_aws_json_1_1(
                item
            )
        )
    return out
