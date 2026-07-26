"""Generated from Smithy shape ``com.amazonaws.configservice#Evaluations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.evaluation

Evaluations: TypeAlias = list["capo_config_service.types.evaluation.Evaluation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Evaluations) -> list:
    import capo_config_service.types.evaluation

    out: list = []
    for item in value:
        out.append(capo_config_service.types.evaluation.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Evaluations:
    import capo_config_service.types.evaluation

    out: Evaluations = []
    for item in data:
        out.append(capo_config_service.types.evaluation.deserialize_aws_json_1_1(item))
    return out
