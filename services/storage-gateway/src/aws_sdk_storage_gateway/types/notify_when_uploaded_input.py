"""Generated from Smithy shape ``com.amazonaws.storagegateway#NotifyWhenUploadedInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_share_arn


class NotifyWhenUploadedInput(TypedDict):
    file_share_arn: "aws_sdk_storage_gateway.types.file_share_arn.FileShareARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotifyWhenUploadedInput) -> dict:
    out: dict = {}
    out["FileShareARN"] = value["file_share_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotifyWhenUploadedInput:
    out: NotifyWhenUploadedInput = {}  # type: ignore[typeddict-item]
    if "FileShareARN" in data:
        out["file_share_arn"] = data["FileShareARN"]
    else:
        raise DeserializationError("NotifyWhenUploadedInput.file_share_arn required")
    return out
