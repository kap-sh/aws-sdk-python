"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileShareInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_share_arn
    import capo_storage_gateway.types.file_share_id
    import capo_storage_gateway.types.file_share_status
    import capo_storage_gateway.types.file_share_type
    import capo_storage_gateway.types.gateway_arn


class FileShareInfo(TypedDict, closed=True):
    file_share_type: NotRequired[
        "capo_storage_gateway.types.file_share_type.FileShareType"
    ]
    file_share_arn: NotRequired[
        "capo_storage_gateway.types.file_share_arn.FileShareARN"
    ]
    file_share_id: NotRequired["capo_storage_gateway.types.file_share_id.FileShareId"]
    file_share_status: NotRequired[
        "capo_storage_gateway.types.file_share_status.FileShareStatus"
    ]
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileShareInfo) -> dict:
    out: dict = {}
    if "file_share_type" in value:
        import capo_storage_gateway.types.file_share_type

        out["FileShareType"] = (
            capo_storage_gateway.types.file_share_type.serialize_aws_json_1_1(
                value["file_share_type"]
            )
        )
    if "file_share_arn" in value:
        out["FileShareARN"] = value["file_share_arn"]
    if "file_share_id" in value:
        out["FileShareId"] = value["file_share_id"]
    if "file_share_status" in value:
        out["FileShareStatus"] = value["file_share_status"]
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileShareInfo:
    out: FileShareInfo = {}  # type: ignore[typeddict-item]
    if "FileShareType" in data:
        import capo_storage_gateway.types.file_share_type

        out["file_share_type"] = (
            capo_storage_gateway.types.file_share_type.deserialize_aws_json_1_1(
                data["FileShareType"]
            )
        )
    if "FileShareARN" in data:
        out["file_share_arn"] = data["FileShareARN"]
    if "FileShareId" in data:
        out["file_share_id"] = data["FileShareId"]
    if "FileShareStatus" in data:
        out["file_share_status"] = data["FileShareStatus"]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    return out
