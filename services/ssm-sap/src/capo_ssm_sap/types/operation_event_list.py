"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_sap.types.operation_event

OperationEventList: TypeAlias = list[
    "capo_ssm_sap.types.operation_event.OperationEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: OperationEventList) -> list:
    import capo_ssm_sap.types.operation_event

    out: list = []
    for item in value:
        out.append(capo_ssm_sap.types.operation_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> OperationEventList:
    import capo_ssm_sap.types.operation_event

    out: OperationEventList = []
    for item in data:
        out.append(capo_ssm_sap.types.operation_event.deserialize_json(item))
    return out
