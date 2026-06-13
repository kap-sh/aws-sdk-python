"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instance_id

RecoveryInstanceIDs: TypeAlias = list[
    "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> RecoveryInstanceIDs:
    return list(data)
