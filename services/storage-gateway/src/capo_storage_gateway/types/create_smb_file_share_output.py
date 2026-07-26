"""Generated from Smithy shape ``com.amazonaws.storagegateway#CreateSMBFileShareOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.file_share_arn


class CreateSMBFileShareOutput(TypedDict, closed=True):
    file_share_arn: NotRequired[
        "capo_storage_gateway.types.file_share_arn.FileShareARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the newly created file share.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSMBFileShareOutput) -> dict:
    out: dict = {}
    if "file_share_arn" in value:
        out["FileShareARN"] = value["file_share_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSMBFileShareOutput:
    out: CreateSMBFileShareOutput = {}  # type: ignore[typeddict-item]
    if "FileShareARN" in data:
        out["file_share_arn"] = data["FileShareARN"]
    return out
