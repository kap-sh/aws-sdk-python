"""Generated from Smithy shape ``com.amazonaws.machinelearning#MLModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.ml_model

MLModels: TypeAlias = list["aws_sdk_machine_learning.types.ml_model.MLModel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MLModels) -> list:
    import aws_sdk_machine_learning.types.ml_model

    out: list = []
    for item in value:
        out.append(aws_sdk_machine_learning.types.ml_model.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MLModels:
    import aws_sdk_machine_learning.types.ml_model

    out: MLModels = []
    for item in data:
        out.append(
            aws_sdk_machine_learning.types.ml_model.deserialize_aws_json_1_1(item)
        )
    return out
