"""Generated from Smithy shape ``com.amazonaws.batch#EvaluateOnExitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.evaluate_on_exit

EvaluateOnExitList: TypeAlias = list[
    "aws_sdk_batch.types.evaluate_on_exit.EvaluateOnExit"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateOnExitList) -> list:
    import aws_sdk_batch.types.evaluate_on_exit

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.evaluate_on_exit.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluateOnExitList:
    import aws_sdk_batch.types.evaluate_on_exit

    out: EvaluateOnExitList = []
    for item in data:
        out.append(aws_sdk_batch.types.evaluate_on_exit.deserialize_json(item))
    return out
