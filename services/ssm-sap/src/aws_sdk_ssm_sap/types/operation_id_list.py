"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.operation_id

OperationIdList: TypeAlias = list["aws_sdk_ssm_sap.types.operation_id.OperationId"]


# --- restJson1 ser/de ---
def serialize_json(value: OperationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> OperationIdList:
    return list(data)
