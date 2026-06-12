"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentRepositorySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.dev_environment_repository_summary

DevEnvironmentRepositorySummaries: TypeAlias = list[
    "aws_sdk_codecatalyst.types.dev_environment_repository_summary.DevEnvironmentRepositorySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentRepositorySummaries) -> list:
    import aws_sdk_codecatalyst.types.dev_environment_repository_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecatalyst.types.dev_environment_repository_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DevEnvironmentRepositorySummaries:
    import aws_sdk_codecatalyst.types.dev_environment_repository_summary

    out: DevEnvironmentRepositorySummaries = []
    for item in data:
        out.append(
            aws_sdk_codecatalyst.types.dev_environment_repository_summary.deserialize_json(
                item
            )
        )
    return out
