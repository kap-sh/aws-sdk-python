"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineParameterSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controltower.types.enabled_baseline_parameter_summary

EnabledBaselineParameterSummaries: TypeAlias = list[
    "aws_sdk_controltower.types.enabled_baseline_parameter_summary.EnabledBaselineParameterSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineParameterSummaries) -> list:
    import aws_sdk_controltower.types.enabled_baseline_parameter_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_controltower.types.enabled_baseline_parameter_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EnabledBaselineParameterSummaries:
    import aws_sdk_controltower.types.enabled_baseline_parameter_summary

    out: EnabledBaselineParameterSummaries = []
    for item in data:
        out.append(
            aws_sdk_controltower.types.enabled_baseline_parameter_summary.deserialize_json(
                item
            )
        )
    return out
