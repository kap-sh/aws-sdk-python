"""Generated from Smithy shape ``com.amazonaws.glacier#GetVaultNotificationsInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class GetVaultNotificationsInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVaultNotificationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetVaultNotificationsInput:
    out: GetVaultNotificationsInput = {}  # type: ignore[typeddict-item]
    return out
