"""Generated from Smithy shape ``com.amazonaws.athena#SessionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.session_summary

SessionsList: TypeAlias = list["aws_sdk_athena.types.session_summary.SessionSummary"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SessionsList) -> list:
    import aws_sdk_athena.types.session_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.session_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SessionsList:
    import aws_sdk_athena.types.session_summary

    out: SessionsList = []
    for item in data:
        out.append(aws_sdk_athena.types.session_summary.deserialize_aws_json_1_1(item))
    return out
