"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.operation

OperationList: TypeAlias = list["aws_sdk_ssm_sap.types.operation.Operation"]


# --- restJson1 ser/de ---
def serialize_json(value: OperationList) -> list:
    import aws_sdk_ssm_sap.types.operation

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> OperationList:
    import aws_sdk_ssm_sap.types.operation

    out: OperationList = []
    for item in data:
        out.append(aws_sdk_ssm_sap.types.operation.deserialize_json(item))
    return out
