"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionSnapshotResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_execution_snapshot_resource

LifecycleExecutionSnapshotResourceList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.lifecycle_execution_snapshot_resource.LifecycleExecutionSnapshotResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionSnapshotResourceList) -> list:
    import aws_sdk_imagebuilder.types.lifecycle_execution_snapshot_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_execution_snapshot_resource.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LifecycleExecutionSnapshotResourceList:
    import aws_sdk_imagebuilder.types.lifecycle_execution_snapshot_resource

    out: LifecycleExecutionSnapshotResourceList = []
    for item in data:
        out.append(
            aws_sdk_imagebuilder.types.lifecycle_execution_snapshot_resource.deserialize_json(
                item
            )
        )
    return out
