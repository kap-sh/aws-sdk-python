"""Generated from Smithy shape ``com.amazonaws.athena#SessionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.session_summary

SessionsList: TypeAlias = list["capo_athena.types.session_summary.SessionSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionsList) -> list:
    import capo_athena.types.session_summary

    out: list = []
    for item in value:
        out.append(capo_athena.types.session_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SessionsList:
    import capo_athena.types.session_summary

    out: SessionsList = []
    for item in data:
        out.append(capo_athena.types.session_summary.deserialize_aws_json_1_1(item))
    return out
