"""Generated from Smithy shape ``com.amazonaws.ecs#LocalStorageTypeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.local_storage_type

LocalStorageTypeSet: TypeAlias = list[
    "aws_sdk_ecs.types.local_storage_type.LocalStorageType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocalStorageTypeSet) -> list:
    import aws_sdk_ecs.types.local_storage_type

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.local_storage_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocalStorageTypeSet:
    import aws_sdk_ecs.types.local_storage_type

    out: LocalStorageTypeSet = []
    for item in data:
        out.append(aws_sdk_ecs.types.local_storage_type.deserialize_aws_json_1_1(item))
    return out
