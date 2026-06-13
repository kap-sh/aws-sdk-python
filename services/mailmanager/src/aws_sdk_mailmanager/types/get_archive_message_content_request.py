"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveMessageContentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.archived_message_id


class GetArchiveMessageContentRequest(TypedDict):
    archived_message_id: (
        "aws_sdk_mailmanager.types.archived_message_id.ArchivedMessageId"
    )
    """<p>The unique identifier of the archived email message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveMessageContentRequest) -> dict:
    out: dict = {}
    out["ArchivedMessageId"] = value["archived_message_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveMessageContentRequest:
    out: GetArchiveMessageContentRequest = {}  # type: ignore[typeddict-item]
    if "ArchivedMessageId" in data:
        out["archived_message_id"] = data["ArchivedMessageId"]
    else:
        raise DeserializationError(
            "GetArchiveMessageContentRequest.archived_message_id required"
        )
    return out
