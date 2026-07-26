"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#OperationStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudcontrol.types.operation_status

OperationStatuses: TypeAlias = list[
    "capo_cloudcontrol.types.operation_status.OperationStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OperationStatuses) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> OperationStatuses:
    return list(data)
