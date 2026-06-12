"""Generated from Smithy shape ``com.amazonaws.xray#FaultRootCauses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.fault_root_cause

FaultRootCauses: TypeAlias = list["aws_sdk_xray.types.fault_root_cause.FaultRootCause"]


# --- restJson1 ser/de ---
def serialize_json(value: FaultRootCauses) -> list:
    import aws_sdk_xray.types.fault_root_cause

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.fault_root_cause.serialize_json(item))
    return out


def deserialize_json(data: list) -> FaultRootCauses:
    import aws_sdk_xray.types.fault_root_cause

    out: FaultRootCauses = []
    for item in data:
        out.append(aws_sdk_xray.types.fault_root_cause.deserialize_json(item))
    return out
