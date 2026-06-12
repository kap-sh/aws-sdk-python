"""Generated from Smithy shape ``com.amazonaws.machinelearning#Evaluations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.evaluation

Evaluations: TypeAlias = list["aws_sdk_machine_learning.types.evaluation.Evaluation"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Evaluations) -> list:
    import aws_sdk_machine_learning.types.evaluation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_machine_learning.types.evaluation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Evaluations:
    import aws_sdk_machine_learning.types.evaluation

    out: Evaluations = []
    for item in data:
        out.append(
            aws_sdk_machine_learning.types.evaluation.deserialize_aws_json_1_1(item)
        )
    return out
