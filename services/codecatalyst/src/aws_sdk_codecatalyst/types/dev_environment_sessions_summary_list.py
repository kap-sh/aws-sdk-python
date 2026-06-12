"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentSessionsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.dev_environment_session_summary

DevEnvironmentSessionsSummaryList: TypeAlias = list[
    "aws_sdk_codecatalyst.types.dev_environment_session_summary.DevEnvironmentSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentSessionsSummaryList) -> list:
    import aws_sdk_codecatalyst.types.dev_environment_session_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecatalyst.types.dev_environment_session_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DevEnvironmentSessionsSummaryList:
    import aws_sdk_codecatalyst.types.dev_environment_session_summary

    out: DevEnvironmentSessionsSummaryList = []
    for item in data:
        out.append(
            aws_sdk_codecatalyst.types.dev_environment_session_summary.deserialize_json(
                item
            )
        )
    return out
