"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileSystemAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_system_association_arn
    import capo_storage_gateway.types.file_system_association_id
    import capo_storage_gateway.types.file_system_association_status
    import capo_storage_gateway.types.gateway_arn


class FileSystemAssociationSummary(TypedDict, closed=True):
    file_system_association_id: NotRequired[
        "capo_storage_gateway.types.file_system_association_id.FileSystemAssociationId"
    ]
    """<p>The ID of the file system association.</p>"""
    file_system_association_arn: NotRequired[
        "capo_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the file system association.</p>"""
    file_system_association_status: NotRequired[
        "capo_storage_gateway.types.file_system_association_status.FileSystemAssociationStatus"
    ]
    """<p>The status of the file share. Valid Values: <code>AVAILABLE</code> | <code>CREATING</code> | <code>DELETING</code> | <code>FORCE_DELETING</code> | <code>UPDATING</code> | <code>ERROR</code> </p>"""
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemAssociationSummary) -> dict:
    out: dict = {}
    if "file_system_association_id" in value:
        out["FileSystemAssociationId"] = value["file_system_association_id"]
    if "file_system_association_arn" in value:
        out["FileSystemAssociationARN"] = value["file_system_association_arn"]
    if "file_system_association_status" in value:
        out["FileSystemAssociationStatus"] = value["file_system_association_status"]
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemAssociationSummary:
    out: FileSystemAssociationSummary = {}  # type: ignore[typeddict-item]
    if "FileSystemAssociationId" in data:
        out["file_system_association_id"] = data["FileSystemAssociationId"]
    if "FileSystemAssociationARN" in data:
        out["file_system_association_arn"] = data["FileSystemAssociationARN"]
    if "FileSystemAssociationStatus" in data:
        out["file_system_association_status"] = data["FileSystemAssociationStatus"]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    return out
