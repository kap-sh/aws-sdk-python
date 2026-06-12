"""Generated from Smithy shape ``com.amazonaws.machinelearning#BatchPredictions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.batch_prediction

BatchPredictions: TypeAlias = list[
    "aws_sdk_machine_learning.types.batch_prediction.BatchPrediction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPredictions) -> list:
    import aws_sdk_machine_learning.types.batch_prediction

    out: list = []
    for item in value:
        out.append(
            aws_sdk_machine_learning.types.batch_prediction.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchPredictions:
    import aws_sdk_machine_learning.types.batch_prediction

    out: BatchPredictions = []
    for item in data:
        out.append(
            aws_sdk_machine_learning.types.batch_prediction.deserialize_aws_json_1_1(
                item
            )
        )
    return out
