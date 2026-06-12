"""Generated from Smithy shape ``com.amazonaws.xray#ErrorRootCauses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.error_root_cause

ErrorRootCauses: TypeAlias = list["aws_sdk_xray.types.error_root_cause.ErrorRootCause"]


# --- restJson1 ser/de ---
def serialize_json(value: ErrorRootCauses) -> list:
    import aws_sdk_xray.types.error_root_cause

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.error_root_cause.serialize_json(item))
    return out


def deserialize_json(data: list) -> ErrorRootCauses:
    import aws_sdk_xray.types.error_root_cause

    out: ErrorRootCauses = []
    for item in data:
        out.append(aws_sdk_xray.types.error_root_cause.deserialize_json(item))
    return out
