"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_execution_resource

LifecycleExecutionResourceList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.lifecycle_execution_resource.LifecycleExecutionResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionResourceList) -> list:
    import aws_sdk_imagebuilder.types.lifecycle_execution_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_execution_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LifecycleExecutionResourceList:
    import aws_sdk_imagebuilder.types.lifecycle_execution_resource

    out: LifecycleExecutionResourceList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_execution_resource.deserialize_json(
                item
            )
        )
    return out
