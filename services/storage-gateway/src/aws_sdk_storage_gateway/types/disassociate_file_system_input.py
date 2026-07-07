"""Generated from Smithy shape ``com.amazonaws.storagegateway#DisassociateFileSystemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.boolean2
    import aws_sdk_storage_gateway.types.file_system_association_arn


class DisassociateFileSystemInput(TypedDict, closed=True):
    file_system_association_arn: "aws_sdk_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
    """<p>The Amazon Resource Name (ARN) of the file system association to be deleted.</p>"""
    force_delete: "aws_sdk_storage_gateway.types.boolean2.Boolean2"
    """<p>If this value is set to true, the operation disassociates an Amazon FSx file system immediately. It ends all data uploads to the file system, and the file system association enters the <code>FORCE_DELETING</code> status. If this value is set to false, the Amazon FSx file system does not disassociate until all data is uploaded.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFileSystemInput) -> dict:
    out: dict = {}
    out["FileSystemAssociationARN"] = value["file_system_association_arn"]
    out["ForceDelete"] = value.get("force_delete", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFileSystemInput:
    out: DisassociateFileSystemInput = {}  # type: ignore[typeddict-item]
    if "FileSystemAssociationARN" in data:
        out["file_system_association_arn"] = data["FileSystemAssociationARN"]
    else:
        raise DeserializationError(
            "DisassociateFileSystemInput.file_system_association_arn required"
        )
    if "ForceDelete" in data:
        out["force_delete"] = data["ForceDelete"]
    else:
        out["force_delete"] = False
    return out
