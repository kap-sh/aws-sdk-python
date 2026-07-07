"""Generated from Smithy shape ``com.amazonaws.storagegateway#RefreshCacheOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_share_arn
    import aws_sdk_storage_gateway.types.notification_id


class RefreshCacheOutput(TypedDict, closed=True):
    file_share_arn: NotRequired[
        "aws_sdk_storage_gateway.types.file_share_arn.FileShareARN"
    ]
    notification_id: NotRequired[
        "aws_sdk_storage_gateway.types.notification_id.NotificationId"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RefreshCacheOutput) -> dict:
    out: dict = {}
    if "file_share_arn" in value:
        out["FileShareARN"] = value["file_share_arn"]
    if "notification_id" in value:
        out["NotificationId"] = value["notification_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RefreshCacheOutput:
    out: RefreshCacheOutput = {}  # type: ignore[typeddict-item]
    if "FileShareARN" in data:
        out["file_share_arn"] = data["FileShareARN"]
    if "NotificationId" in data:
        out["notification_id"] = data["NotificationId"]
    return out
