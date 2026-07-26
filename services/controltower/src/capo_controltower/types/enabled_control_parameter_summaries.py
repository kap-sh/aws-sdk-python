"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlParameterSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.enabled_control_parameter_summary

EnabledControlParameterSummaries: TypeAlias = list[
    "capo_controltower.types.enabled_control_parameter_summary.EnabledControlParameterSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlParameterSummaries) -> list:
    import capo_controltower.types.enabled_control_parameter_summary

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.enabled_control_parameter_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnabledControlParameterSummaries:
    import capo_controltower.types.enabled_control_parameter_summary

    out: EnabledControlParameterSummaries = []
    for item in data:
        out.append(
            capo_controltower.types.enabled_control_parameter_summary.deserialize_json(
                item
            )
        )
    return out
