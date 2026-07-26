"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.dev_environment_summary

DevEnvironmentSummaryList: TypeAlias = list[
    "capo_codecatalyst.types.dev_environment_summary.DevEnvironmentSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentSummaryList) -> list:
    import capo_codecatalyst.types.dev_environment_summary

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.dev_environment_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DevEnvironmentSummaryList:
    import capo_codecatalyst.types.dev_environment_summary

    out: DevEnvironmentSummaryList = []
    for item in data:
        out.append(
            capo_codecatalyst.types.dev_environment_summary.deserialize_json(item)
        )
    return out
