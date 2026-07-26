"""Generated from Smithy shape ``com.amazonaws.controltower#Baselines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.baseline_summary

Baselines: TypeAlias = list["capo_controltower.types.baseline_summary.BaselineSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: Baselines) -> list:
    import capo_controltower.types.baseline_summary

    out: list = []
    for item in value:
        out.append(capo_controltower.types.baseline_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Baselines:
    import capo_controltower.types.baseline_summary

    out: Baselines = []
    for item in data:
        out.append(capo_controltower.types.baseline_summary.deserialize_json(item))
    return out
