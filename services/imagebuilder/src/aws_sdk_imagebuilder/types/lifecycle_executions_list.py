"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_execution

LifecycleExecutionsList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.lifecycle_execution.LifecycleExecution"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionsList) -> list:
    import aws_sdk_imagebuilder.types.lifecycle_execution

    out: list = []
    for item in value:
        out.append(aws_sdk_imagebuilder.types.lifecycle_execution.serialize_json(item))
    return out


def deserialize_json(data: list) -> LifecycleExecutionsList:
    import aws_sdk_imagebuilder.types.lifecycle_execution

    out: LifecycleExecutionsList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_execution.deserialize_json(item)
        )
    return out
