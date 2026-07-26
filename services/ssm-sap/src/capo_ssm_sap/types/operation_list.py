"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_sap.types.operation

OperationList: TypeAlias = list["capo_ssm_sap.types.operation.Operation"]


# --- restJson1 ser/de ---
def serialize_json(value: OperationList) -> list:
    import capo_ssm_sap.types.operation

    out: list = []
    for item in value:
        out.append(capo_ssm_sap.types.operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> OperationList:
    import capo_ssm_sap.types.operation

    out: OperationList = []
    for item in data:
        out.append(capo_ssm_sap.types.operation.deserialize_json(item))
    return out
