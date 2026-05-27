"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesStorageConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.task_volume_storage_gi_b


class ManagedInstancesStorageConfiguration(TypedDict):
    storage_size_gi_b: NotRequired[
        "aws_sdk_ecs.types.task_volume_storage_gi_b.TaskVolumeStorageGiB"
    ]
    """<p>The size of the data volume.</p>"""
