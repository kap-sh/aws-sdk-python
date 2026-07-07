"""Generated from Smithy shape ``com.amazonaws.athena#NotebookSessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.date
    import aws_sdk_athena.types.session_id


class NotebookSessionSummary(TypedDict, closed=True):
    session_id: NotRequired["aws_sdk_athena.types.session_id.SessionId"]
    """<p>The notebook session ID.</p>"""
    creation_time: NotRequired["aws_sdk_athena.types.date.Date"]
    """<p>The time when the notebook session was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookSessionSummary) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "creation_time" in value:
        import aws_sdk_athena.types.date

        out["CreationTime"] = aws_sdk_athena.types.date.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookSessionSummary:
    out: NotebookSessionSummary = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    if "CreationTime" in data:
        import aws_sdk_athena.types.date

        out["creation_time"] = aws_sdk_athena.types.date.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
