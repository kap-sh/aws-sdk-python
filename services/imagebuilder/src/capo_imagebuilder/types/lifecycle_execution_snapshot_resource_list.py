"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecycleExecutionSnapshotResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.lifecycle_execution_snapshot_resource

LifecycleExecutionSnapshotResourceList: TypeAlias = list[
    "capo_imagebuilder.types.lifecycle_execution_snapshot_resource.LifecycleExecutionSnapshotResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleExecutionSnapshotResourceList) -> list:
    import capo_imagebuilder.types.lifecycle_execution_snapshot_resource

    out: list = []
    for item in value:
        out.append(
            capo_imagebuilder.types.lifecycle_execution_snapshot_resource.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LifecycleExecutionSnapshotResourceList:
    import capo_imagebuilder.types.lifecycle_execution_snapshot_resource

    out: LifecycleExecutionSnapshotResourceList = []
    for item in data:
        out.append(
            capo_imagebuilder.types.lifecycle_execution_snapshot_resource.deserialize_json(
                item
            )
        )
    return out
