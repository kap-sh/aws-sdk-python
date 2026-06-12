"""Generated from Smithy shape ``com.amazonaws.glacier#CompleteMultipartUploadInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class CompleteMultipartUploadInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    upload_id: "aws_sdk_glacier.types.string.string"
    """<p>The upload ID of the multipart upload.</p>"""
    archive_size: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The total size, in bytes, of the entire archive. This value should be the sum of all the sizes of the individual parts that you uploaded.</p>"""
    checksum: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The SHA256 tree hash of the entire archive. It is the tree hash of SHA256 tree hash of the individual parts. If the value you specify in the request does not match the SHA256 tree hash of the final assembled archive as computed by Amazon Glacier (Glacier), Glacier returns an error and the request fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteMultipartUploadInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CompleteMultipartUploadInput:
    out: CompleteMultipartUploadInput = {}  # type: ignore[typeddict-item]
    return out
