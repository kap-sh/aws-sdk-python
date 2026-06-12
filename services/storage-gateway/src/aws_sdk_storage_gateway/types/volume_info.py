"""Generated from Smithy shape ``com.amazonaws.storagegateway#VolumeInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.gateway_id
    import aws_sdk_storage_gateway.types.long
    import aws_sdk_storage_gateway.types.volume_arn
    import aws_sdk_storage_gateway.types.volume_attachment_status
    import aws_sdk_storage_gateway.types.volume_id
    import aws_sdk_storage_gateway.types.volume_type


class VolumeInfo(TypedDict):
    volume_arn: NotRequired["aws_sdk_storage_gateway.types.volume_arn.VolumeARN"]
    """<p>The Amazon Resource Name (ARN) for the storage volume. For example, the following is a valid ARN:</p> <p> <code>arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABB</code> </p> <p>Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).</p>"""
    volume_id: NotRequired["aws_sdk_storage_gateway.types.volume_id.VolumeId"]
    """<p>The unique identifier assigned to the volume. This ID becomes part of the volume Amazon Resource Name (ARN), which you use as input for other operations.</p> <p>Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).</p>"""
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    gateway_id: NotRequired["aws_sdk_storage_gateway.types.gateway_id.GatewayId"]
    """<p>The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.</p> <p>Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).</p>"""
    volume_type: NotRequired["aws_sdk_storage_gateway.types.volume_type.VolumeType"]
    """<p>One of the VolumeType enumeration values describing the type of the volume.</p>"""
    volume_size_in_bytes: "aws_sdk_storage_gateway.types.long.long"
    """<p>The size of the volume in bytes.</p> <p>Valid Values: 50 to 500 lowercase letters, numbers, periods (.), and hyphens (-).</p>"""
    volume_attachment_status: NotRequired[
        "aws_sdk_storage_gateway.types.volume_attachment_status.VolumeAttachmentStatus"
    ]
    """<p>One of the VolumeStatus values that indicates the state of the storage volume.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VolumeInfo) -> dict:
    out: dict = {}
    if "volume_arn" in value:
        out["VolumeARN"] = value["volume_arn"]
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "gateway_id" in value:
        out["GatewayId"] = value["gateway_id"]
    if "volume_type" in value:
        out["VolumeType"] = value["volume_type"]
    out["VolumeSizeInBytes"] = value.get("volume_size_in_bytes", 0)
    if "volume_attachment_status" in value:
        out["VolumeAttachmentStatus"] = value["volume_attachment_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VolumeInfo:
    out: VolumeInfo = {}  # type: ignore[typeddict-item]
    if "VolumeARN" in data:
        out["volume_arn"] = data["VolumeARN"]
    if "VolumeId" in data:
        out["volume_id"] = data["VolumeId"]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "GatewayId" in data:
        out["gateway_id"] = data["GatewayId"]
    if "VolumeType" in data:
        out["volume_type"] = data["VolumeType"]
    if "VolumeSizeInBytes" in data:
        out["volume_size_in_bytes"] = data["VolumeSizeInBytes"]
    else:
        out["volume_size_in_bytes"] = 0
    if "VolumeAttachmentStatus" in data:
        out["volume_attachment_status"] = data["VolumeAttachmentStatus"]
    return out
