"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDisks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_instance_disk

RecoveryInstanceDisks: TypeAlias = list[
    "capo_drs.types.recovery_instance_disk.RecoveryInstanceDisk"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDisks) -> list:
    import capo_drs.types.recovery_instance_disk

    out: list = []
    for item in value:
        out.append(capo_drs.types.recovery_instance_disk.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecoveryInstanceDisks:
    import capo_drs.types.recovery_instance_disk

    out: RecoveryInstanceDisks = []
    for item in data:
        out.append(capo_drs.types.recovery_instance_disk.deserialize_json(item))
    return out
