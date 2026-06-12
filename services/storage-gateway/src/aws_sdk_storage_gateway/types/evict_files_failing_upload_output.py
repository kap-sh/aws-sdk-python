"""Generated from Smithy shape ``com.amazonaws.storagegateway#EvictFilesFailingUploadOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.string


class EvictFilesFailingUploadOutput(TypedDict):
    notification_id: NotRequired["aws_sdk_storage_gateway.types.string.string"]
    """<p>The randomly generated ID of the CloudWatch notification associated with the cache clean operation. This ID is in UUID format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvictFilesFailingUploadOutput) -> dict:
    out: dict = {}
    if "notification_id" in value:
        out["NotificationId"] = value["notification_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EvictFilesFailingUploadOutput:
    out: EvictFilesFailingUploadOutput = {}  # type: ignore[typeddict-item]
    if "NotificationId" in data:
        out["notification_id"] = data["NotificationId"]
    return out
