"""Generated from Smithy shape ``com.amazonaws.pipes#BatchEnvironmentVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pipes.types.batch_environment_variable

BatchEnvironmentVariableList: TypeAlias = list[
    "aws_sdk_pipes.types.batch_environment_variable.BatchEnvironmentVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchEnvironmentVariableList) -> list:
    import aws_sdk_pipes.types.batch_environment_variable

    out: list = []
    for item in value:
        out.append(aws_sdk_pipes.types.batch_environment_variable.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchEnvironmentVariableList:
    import aws_sdk_pipes.types.batch_environment_variable

    out: BatchEnvironmentVariableList = []
    for item in data:
        out.append(
            aws_sdk_pipes.types.batch_environment_variable.deserialize_json(item)
        )
    return out
