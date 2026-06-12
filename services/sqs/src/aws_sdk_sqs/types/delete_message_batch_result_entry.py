"""Generated from Smithy shape ``com.amazonaws.sqs#DeleteMessageBatchResultEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sqs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sqs.types.string


class DeleteMessageBatchResultEntry(TypedDict):
    id: "aws_sdk_sqs.types.string.String"
    """<p>Represents a successfully deleted message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMessageBatchResultEntry) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMessageBatchResultEntry:
    out: DeleteMessageBatchResultEntry = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DeleteMessageBatchResultEntry.id required")
    return out
