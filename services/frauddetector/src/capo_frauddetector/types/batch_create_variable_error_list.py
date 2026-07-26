"""Generated from Smithy shape ``com.amazonaws.frauddetector#BatchCreateVariableErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.batch_create_variable_error

BatchCreateVariableErrorList: TypeAlias = list[
    "capo_frauddetector.types.batch_create_variable_error.BatchCreateVariableError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCreateVariableErrorList) -> list:
    import capo_frauddetector.types.batch_create_variable_error

    out: list = []
    for item in value:
        out.append(
            capo_frauddetector.types.batch_create_variable_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BatchCreateVariableErrorList:
    import capo_frauddetector.types.batch_create_variable_error

    out: BatchCreateVariableErrorList = []
    for item in data:
        out.append(
            capo_frauddetector.types.batch_create_variable_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
