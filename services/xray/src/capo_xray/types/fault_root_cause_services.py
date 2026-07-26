"""Generated from Smithy shape ``com.amazonaws.xray#FaultRootCauseServices``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.fault_root_cause_service

FaultRootCauseServices: TypeAlias = list[
    "capo_xray.types.fault_root_cause_service.FaultRootCauseService"
]


# --- restJson1 ser/de ---
def serialize_json(value: FaultRootCauseServices) -> list:
    import capo_xray.types.fault_root_cause_service

    out: list = []
    for item in value:
        out.append(capo_xray.types.fault_root_cause_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> FaultRootCauseServices:
    import capo_xray.types.fault_root_cause_service

    out: FaultRootCauseServices = []
    for item in data:
        out.append(capo_xray.types.fault_root_cause_service.deserialize_json(item))
    return out
