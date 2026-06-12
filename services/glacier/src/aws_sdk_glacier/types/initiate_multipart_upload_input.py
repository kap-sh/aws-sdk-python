"""Generated from Smithy shape ``com.amazonaws.glacier#InitiateMultipartUploadInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class InitiateMultipartUploadInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    archive_description: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The archive description that you are uploading in parts.</p> <p>The part size must be a megabyte (1024 KB) multiplied by a power of 2, for example 1048576 (1 MB), 2097152 (2 MB), 4194304 (4 MB), 8388608 (8 MB), and so on. The minimum allowable part size is 1 MB, and the maximum is 4 GB (4096 MB).</p>"""
    part_size: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The size of each part except the last, in bytes. The last part can be smaller than this part size.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateMultipartUploadInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> InitiateMultipartUploadInput:
    out: InitiateMultipartUploadInput = {}  # type: ignore[typeddict-item]
    return out
