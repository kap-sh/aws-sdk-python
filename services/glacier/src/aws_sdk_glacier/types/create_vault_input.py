"""Generated from Smithy shape ``com.amazonaws.glacier#CreateVaultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class CreateVaultInput(TypedDict, closed=True):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVaultInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateVaultInput:
    out: CreateVaultInput = {}  # type: ignore[typeddict-item]
    return out
