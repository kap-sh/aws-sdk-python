"""Generated from Smithy shape ``com.amazonaws.datazone#ComputeEnvironmentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.compute_environments

ComputeEnvironmentsList: TypeAlias = list[
    "aws_sdk_datazone.types.compute_environments.ComputeEnvironments"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeEnvironmentsList) -> list:
    import aws_sdk_datazone.types.compute_environments

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.compute_environments.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComputeEnvironmentsList:
    import aws_sdk_datazone.types.compute_environments

    out: ComputeEnvironmentsList = []
    for item in data:
        out.append(aws_sdk_datazone.types.compute_environments.deserialize_json(item))
    return out
