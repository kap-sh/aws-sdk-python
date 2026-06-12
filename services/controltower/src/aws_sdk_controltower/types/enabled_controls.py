"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_control_summary

EnabledControls: TypeAlias = list[
    "aws_sdk_controltower.types.enabled_control_summary.EnabledControlSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControls) -> list:
    import aws_sdk_controltower.types.enabled_control_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controltower.types.enabled_control_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnabledControls:
    import aws_sdk_controltower.types.enabled_control_summary

    out: EnabledControls = []
    for item in data:
        out.append(
            aws_sdk_controltower.types.enabled_control_summary.deserialize_json(item)
        )
    return out
