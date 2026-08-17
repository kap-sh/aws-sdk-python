"""Generated from Smithy shape ``com.amazonaws.ecs#ManagedInstancesStorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.task_volume_storage_gi_b


class ManagedInstancesStorageConfiguration(TypedDict, closed=True):
    storage_size_gi_b: NotRequired[
        "capo_ecs.types.task_volume_storage_gi_b.TaskVolumeStorageGiB"
    ]
    """<p>The size of the data volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedInstancesStorageConfiguration) -> dict:
    out: dict = {}
    if "storage_size_gi_b" in value:
        out["storageSizeGiB"] = value["storage_size_gi_b"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedInstancesStorageConfiguration:
    out: ManagedInstancesStorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("storageSizeGiB") is not None:
        out["storage_size_gi_b"] = data["storageSizeGiB"]
    return out
