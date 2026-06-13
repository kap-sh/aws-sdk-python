"""Generated from Smithy shape ``com.amazonaws.drs#StartFailbackRequestRecoveryInstanceIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.recovery_instance_id

StartFailbackRequestRecoveryInstanceIDs: TypeAlias = list[
    "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartFailbackRequestRecoveryInstanceIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> StartFailbackRequestRecoveryInstanceIDs:
    return list(data)
