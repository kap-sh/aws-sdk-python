"""Generated from Smithy shape ``com.amazonaws.storagegateway#DisassociateFileSystemOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_arn


class DisassociateFileSystemOutput(TypedDict):
    file_system_association_arn: NotRequired[
        "aws_sdk_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the deleted file system association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateFileSystemOutput) -> dict:
    out: dict = {}
    if "file_system_association_arn" in value:
        out["FileSystemAssociationARN"] = value["file_system_association_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateFileSystemOutput:
    out: DisassociateFileSystemOutput = {}  # type: ignore[typeddict-item]
    if "FileSystemAssociationARN" in data:
        out["file_system_association_arn"] = data["FileSystemAssociationARN"]
    return out
