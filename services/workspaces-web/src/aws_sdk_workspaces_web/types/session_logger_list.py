"""Generated from Smithy shape ``com.amazonaws.workspacesweb#SessionLoggerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.session_logger_summary

SessionLoggerList: TypeAlias = list[
    "aws_sdk_workspaces_web.types.session_logger_summary.SessionLoggerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionLoggerList) -> list:
    import aws_sdk_workspaces_web.types.session_logger_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_web.types.session_logger_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SessionLoggerList:
    import aws_sdk_workspaces_web.types.session_logger_summary

    out: SessionLoggerList = []
    for item in data:
        out.append(
            aws_sdk_workspaces_web.types.session_logger_summary.deserialize_json(item)
        )
    return out
