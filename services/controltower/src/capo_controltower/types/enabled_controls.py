"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.enabled_control_summary

EnabledControls: TypeAlias = list[
    "capo_controltower.types.enabled_control_summary.EnabledControlSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControls) -> list:
    import capo_controltower.types.enabled_control_summary

    out: list = []
    for item in value:
        out.append(capo_controltower.types.enabled_control_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnabledControls:
    import capo_controltower.types.enabled_control_summary

    out: EnabledControls = []
    for item in data:
        out.append(
            capo_controltower.types.enabled_control_summary.deserialize_json(item)
        )
    return out
