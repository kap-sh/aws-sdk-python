"""Generated from Smithy shape ``com.amazonaws.athena#NotebookSessionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.notebook_session_summary

NotebookSessionsList: TypeAlias = list[
    "aws_sdk_athena.types.notebook_session_summary.NotebookSessionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookSessionsList) -> list:
    import aws_sdk_athena.types.notebook_session_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_athena.types.notebook_session_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotebookSessionsList:
    import aws_sdk_athena.types.notebook_session_summary

    out: NotebookSessionsList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.notebook_session_summary.deserialize_aws_json_1_1(item)
        )
    return out
