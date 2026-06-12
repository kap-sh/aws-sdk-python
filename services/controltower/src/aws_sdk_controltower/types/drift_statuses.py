"""Generated from Smithy shape ``com.amazonaws.controltower#DriftStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.drift_status

DriftStatuses: TypeAlias = list["aws_sdk_controltower.types.drift_status.DriftStatus"]


# --- restJson1 ser/de ---
def serialize_json(value: DriftStatuses) -> list:
    import aws_sdk_controltower.types.drift_status

    out: list = []
    for item in value:
        out.append(aws_sdk_controltower.types.drift_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> DriftStatuses:
    import aws_sdk_controltower.types.drift_status

    out: DriftStatuses = []
    for item in data:
        out.append(aws_sdk_controltower.types.drift_status.deserialize_json(item))
    return out
