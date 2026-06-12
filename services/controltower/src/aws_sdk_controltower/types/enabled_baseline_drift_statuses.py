"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDriftStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_baseline_drift_status

EnabledBaselineDriftStatuses: TypeAlias = list[
    "aws_sdk_controltower.types.enabled_baseline_drift_status.EnabledBaselineDriftStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineDriftStatuses) -> list:
    import aws_sdk_controltower.types.enabled_baseline_drift_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controltower.types.enabled_baseline_drift_status.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnabledBaselineDriftStatuses:
    import aws_sdk_controltower.types.enabled_baseline_drift_status

    out: EnabledBaselineDriftStatuses = []
    for item in data:
        out.append(
            aws_sdk_controltower.types.enabled_baseline_drift_status.deserialize_json(
                item
            )
        )
    return out
