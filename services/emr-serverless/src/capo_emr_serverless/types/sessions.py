"""Generated from Smithy shape ``com.amazonaws.emrserverless#Sessions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_serverless.types.session_summary

Sessions: TypeAlias = list["capo_emr_serverless.types.session_summary.SessionSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: Sessions) -> list:
    import capo_emr_serverless.types.session_summary

    out: list = []
    for item in value:
        out.append(capo_emr_serverless.types.session_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Sessions:
    import capo_emr_serverless.types.session_summary

    out: Sessions = []
    for item in data:
        out.append(capo_emr_serverless.types.session_summary.deserialize_json(item))
    return out
