"""Generated from Smithy shape ``com.amazonaws.xray#FaultRootCauseEntityPath``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.fault_root_cause_entity

FaultRootCauseEntityPath: TypeAlias = list[
    "aws_sdk_xray.types.fault_root_cause_entity.FaultRootCauseEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: FaultRootCauseEntityPath) -> list:
    import aws_sdk_xray.types.fault_root_cause_entity

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.fault_root_cause_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> FaultRootCauseEntityPath:
    import aws_sdk_xray.types.fault_root_cause_entity

    out: FaultRootCauseEntityPath = []
    for item in data:
        out.append(aws_sdk_xray.types.fault_root_cause_entity.deserialize_json(item))
    return out
