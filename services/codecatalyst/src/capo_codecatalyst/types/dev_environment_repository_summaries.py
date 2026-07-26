"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentRepositorySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.dev_environment_repository_summary

DevEnvironmentRepositorySummaries: TypeAlias = list[
    "capo_codecatalyst.types.dev_environment_repository_summary.DevEnvironmentRepositorySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentRepositorySummaries) -> list:
    import capo_codecatalyst.types.dev_environment_repository_summary

    out: list = []
    for item in value:
        out.append(
            capo_codecatalyst.types.dev_environment_repository_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DevEnvironmentRepositorySummaries:
    import capo_codecatalyst.types.dev_environment_repository_summary

    out: DevEnvironmentRepositorySummaries = []
    for item in data:
        out.append(
            capo_codecatalyst.types.dev_environment_repository_summary.deserialize_json(
                item
            )
        )
    return out
