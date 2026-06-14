"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateNFSFileShareOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.file_share_arn


class CreateNFSFileShareOutput(TypedDict):
    file_share_arn: NotRequired[
        "aws_sdk_storage_gateway.types.file_share_arn.FileShareARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the newly created file share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNFSFileShareOutput) -> dict:
    out: dict = {}
    if "file_share_arn" in value:
        out["FileShareARN"] = value["file_share_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNFSFileShareOutput:
    out: CreateNFSFileShareOutput = {}  # type: ignore[typeddict-item]
    if "FileShareARN" in data:
        out["file_share_arn"] = data["FileShareARN"]
    return out
