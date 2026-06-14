"""Generated from Smithy shape ``com.amazonaws.workspaces#TerminateWorkspacesPoolSessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.amazon_uuid


class TerminateWorkspacesPoolSessionRequest(TypedDict):
    session_id: "aws_sdk_workspaces.types.amazon_uuid.AmazonUuid"
    """<p>The identifier of the pool session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateWorkspacesPoolSessionRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateWorkspacesPoolSessionRequest:
    out: TerminateWorkspacesPoolSessionRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError(
            "TerminateWorkspacesPoolSessionRequest.session_id required"
        )
    return out
