"""Generated from Smithy shape ``com.amazonaws.glacier#DeleteArchiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class DeleteArchiveInput(TypedDict, closed=True):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    archive_id: "aws_sdk_glacier.types.string.string"
    """<p>The ID of the archive to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteArchiveInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteArchiveInput:
    out: DeleteArchiveInput = {}  # type: ignore[typeddict-item]
    return out
