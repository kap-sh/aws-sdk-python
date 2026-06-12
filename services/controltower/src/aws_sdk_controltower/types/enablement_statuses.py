"""Generated from Smithy shape ``com.amazonaws.controltower#EnablementStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enablement_status

EnablementStatuses: TypeAlias = list[
    "aws_sdk_controltower.types.enablement_status.EnablementStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnablementStatuses) -> list:
    import aws_sdk_controltower.types.enablement_status

    out: list = []
    for item in value:
        out.append(aws_sdk_controltower.types.enablement_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnablementStatuses:
    import aws_sdk_controltower.types.enablement_status

    out: EnablementStatuses = []
    for item in data:
        out.append(aws_sdk_controltower.types.enablement_status.deserialize_json(item))
    return out
