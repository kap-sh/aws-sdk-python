"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baseline_summary

EnabledBaselines: TypeAlias = list[
    "capo_controltower.types.enabled_baseline_summary.EnabledBaselineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselines) -> list:
    import capo_controltower.types.enabled_baseline_summary

    out: list = []
    for item in value:
        out.append(
            capo_controltower.types.enabled_baseline_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EnabledBaselines:
    import capo_controltower.types.enabled_baseline_summary

    out: EnabledBaselines = []
    for item in data:
        out.append(
            capo_controltower.types.enabled_baseline_summary.deserialize_json(item)
        )
    return out
