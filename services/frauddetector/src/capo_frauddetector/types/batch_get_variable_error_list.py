"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchGetVariableErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_get_variable_error

BatchGetVariableErrorList: TypeAlias = list[
    "capo_frauddetector.types.batch_get_variable_error.BatchGetVariableError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetVariableErrorList) -> list:
    import capo_frauddetector.types.batch_get_variable_error

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.batch_get_variable_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchGetVariableErrorList:
    import capo_frauddetector.types.batch_get_variable_error

    out: BatchGetVariableErrorList = []
    for item in data:
        out.append(
            capo_frauddetector.types.batch_get_variable_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
