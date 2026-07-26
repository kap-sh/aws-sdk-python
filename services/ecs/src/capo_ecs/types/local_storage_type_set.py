"""Generated from Smithy shape ``com.amazonaws.ecs#LocalStorageTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.local_storage_type

LocalStorageTypeSet: TypeAlias = list[
    "capo_ecs.types.local_storage_type.LocalStorageType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocalStorageTypeSet) -> list:
    import capo_ecs.types.local_storage_type

    out: list = []
    for item in value:
        out.append(capo_ecs.types.local_storage_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocalStorageTypeSet:
    import capo_ecs.types.local_storage_type

    out: LocalStorageTypeSet = []
    for item in data:
        out.append(capo_ecs.types.local_storage_type.deserialize_aws_json_1_1(item))
    return out
