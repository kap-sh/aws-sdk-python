"""Generated from Smithy shape ``com.amazonaws.m2#EnvironmentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.environment_summary

EnvironmentSummaryList: TypeAlias = list[
    "capo_m2.types.environment_summary.EnvironmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentSummaryList) -> list:
    import capo_m2.types.environment_summary

    out: list = []
    for item in value:
        out.append(capo_m2.types.environment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentSummaryList:
    import capo_m2.types.environment_summary

    out: EnvironmentSummaryList = []
    for item in data:
        out.append(capo_m2.types.environment_summary.deserialize_json(item))
    return out
