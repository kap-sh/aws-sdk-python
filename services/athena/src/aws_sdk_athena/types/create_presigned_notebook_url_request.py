"""Generated from Smithy shape ``com.amazonaws.athena#CreatePresignedNotebookUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.session_id


class CreatePresignedNotebookUrlRequest(TypedDict, closed=True):
    session_id: "aws_sdk_athena.types.session_id.SessionId"
    """<p>The session ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePresignedNotebookUrlRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePresignedNotebookUrlRequest:
    out: CreatePresignedNotebookUrlRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError(
            "CreatePresignedNotebookUrlRequest.session_id required"
        )
    return out
