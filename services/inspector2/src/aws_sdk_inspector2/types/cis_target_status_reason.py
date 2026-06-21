"""Generated from Smithy shape ``com.amazonaws.inspector2#CisTargetStatusReason``."""

from typing import Literal, TypeAlias, cast

CisTargetStatusReason: TypeAlias = Literal[
    "SCAN_IN_PROGRESS",
    "UNSUPPORTED_OS",
    "SSM_UNMANAGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CisTargetStatusReason) -> str:
    return value


def deserialize_json(data: str) -> CisTargetStatusReason:
    return cast(CisTargetStatusReason, data)
