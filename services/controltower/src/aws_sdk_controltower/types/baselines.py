"""Generated from Smithy shape ``com.amazonaws.controltower#Baselines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.baseline_summary

Baselines: TypeAlias = list[
    "aws_sdk_controltower.types.baseline_summary.BaselineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: Baselines) -> list:
    import aws_sdk_controltower.types.baseline_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_controltower.types.baseline_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Baselines:
    import aws_sdk_controltower.types.baseline_summary

    out: Baselines = []
    for item in data:
        out.append(aws_sdk_controltower.types.baseline_summary.deserialize_json(item))
    return out
