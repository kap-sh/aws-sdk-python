"""Generated from Smithy shape ``com.amazonaws.glacier#CompleteVaultLockInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class CompleteVaultLockInput(TypedDict, closed=True):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID. This value must match the AWS account ID associated with the credentials used to sign the request. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you specify your account ID, do not include any hyphens ('-') in the ID.</p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    lock_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>lockId</code> value is the lock ID obtained from a <a>InitiateVaultLock</a> request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteVaultLockInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CompleteVaultLockInput:
    out: CompleteVaultLockInput = {}  # type: ignore[typeddict-item]
    return out
