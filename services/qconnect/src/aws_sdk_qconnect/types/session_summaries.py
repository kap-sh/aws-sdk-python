"""Generated from Smithy shape ``com.amazonaws.qconnect#SessionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.session_summary

SessionSummaries: TypeAlias = list[
    "aws_sdk_qconnect.types.session_summary.SessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummaries) -> list:
    import aws_sdk_qconnect.types.session_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_qconnect.types.session_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SessionSummaries:
    import aws_sdk_qconnect.types.session_summary

    out: SessionSummaries = []
    for item in data:
        out.append(aws_sdk_qconnect.types.session_summary.deserialize_json(item))
    return out
