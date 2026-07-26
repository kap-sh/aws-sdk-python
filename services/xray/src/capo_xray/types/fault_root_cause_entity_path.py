"""Generated from Smithy shape ``com.amazonaws.xray#FaultRootCauseEntityPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_xray.types.fault_root_cause_entity

FaultRootCauseEntityPath: TypeAlias = list[
    "capo_xray.types.fault_root_cause_entity.FaultRootCauseEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: FaultRootCauseEntityPath) -> list:
    import capo_xray.types.fault_root_cause_entity

    out: list = []
    for item in value:
        out.append(capo_xray.types.fault_root_cause_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> FaultRootCauseEntityPath:
    import capo_xray.types.fault_root_cause_entity

    out: FaultRootCauseEntityPath = []
    for item in data:
        out.append(capo_xray.types.fault_root_cause_entity.deserialize_json(item))
    return out
