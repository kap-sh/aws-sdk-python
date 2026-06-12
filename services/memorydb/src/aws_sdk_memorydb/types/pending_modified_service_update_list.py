"""Generated from Smithy shape ``com.amazonaws.memorydb#PendingModifiedServiceUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.pending_modified_service_update

PendingModifiedServiceUpdateList: TypeAlias = list[
    "aws_sdk_memorydb.types.pending_modified_service_update.PendingModifiedServiceUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingModifiedServiceUpdateList) -> list:
    import aws_sdk_memorydb.types.pending_modified_service_update

    out: list = []
    for item in value:
        out.append(
            aws_sdk_memorydb.types.pending_modified_service_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingModifiedServiceUpdateList:
    import aws_sdk_memorydb.types.pending_modified_service_update

    out: PendingModifiedServiceUpdateList = []
    for item in data:
        out.append(
            aws_sdk_memorydb.types.pending_modified_service_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out
