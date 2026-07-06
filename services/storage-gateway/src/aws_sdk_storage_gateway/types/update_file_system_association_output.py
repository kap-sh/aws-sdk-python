"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateFileSystemAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_system_association_arn


class UpdateFileSystemAssociationOutput(TypedDict, closed=True):
    file_system_association_arn: NotRequired[
        "aws_sdk_storage_gateway.types.file_system_association_arn.FileSystemAssociationARN"
    ]
    """<p>The ARN of the updated file system association.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemAssociationOutput) -> dict:
    out: dict = {}
    if "file_system_association_arn" in value:
        out["FileSystemAssociationARN"] = value["file_system_association_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemAssociationOutput:
    out: UpdateFileSystemAssociationOutput = {}  # type: ignore[typeddict-item]
    if "FileSystemAssociationARN" in data:
        out["file_system_association_arn"] = data["FileSystemAssociationARN"]
    return out
