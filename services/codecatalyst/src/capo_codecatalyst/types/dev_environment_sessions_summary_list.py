"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentSessionsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.dev_environment_session_summary

DevEnvironmentSessionsSummaryList: TypeAlias = list[
    "capo_codecatalyst.types.dev_environment_session_summary.DevEnvironmentSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentSessionsSummaryList) -> list:
    import capo_codecatalyst.types.dev_environment_session_summary

    out: list = []
    for item in value:
        out.append(
            capo_codecatalyst.types.dev_environment_session_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DevEnvironmentSessionsSummaryList:
    import capo_codecatalyst.types.dev_environment_session_summary

    out: DevEnvironmentSessionsSummaryList = []
    for item in data:
        out.append(
            capo_codecatalyst.types.dev_environment_session_summary.deserialize_json(
                item
            )
        )
    return out
