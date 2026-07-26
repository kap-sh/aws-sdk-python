"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateNFSFileShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_share_arn


class UpdateNFSFileShareOutput(TypedDict, closed=True):
    file_share_arn: NotRequired[
        "capo_storage_gateway.types.file_share_arn.FileShareARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the updated file share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNFSFileShareOutput) -> dict:
    out: dict = {}
    if "file_share_arn" in value:
        out["FileShareARN"] = value["file_share_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNFSFileShareOutput:
    out: UpdateNFSFileShareOutput = {}  # type: ignore[typeddict-item]
    if "FileShareARN" in data:
        out["file_share_arn"] = data["FileShareARN"]
    return out
