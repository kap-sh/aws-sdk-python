"""Generated from Smithy shape ``com.amazonaws.pipes#BatchEnvironmentVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.batch_environment_variable

BatchEnvironmentVariableList: TypeAlias = list[
    "capo_pipes.types.batch_environment_variable.BatchEnvironmentVariable"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchEnvironmentVariableList) -> list:
    import capo_pipes.types.batch_environment_variable

    out: list = []
    for item in value:
        out.append(capo_pipes.types.batch_environment_variable.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchEnvironmentVariableList:
    import capo_pipes.types.batch_environment_variable

    out: BatchEnvironmentVariableList = []
    for item in data:
        out.append(capo_pipes.types.batch_environment_variable.deserialize_json(item))
    return out
