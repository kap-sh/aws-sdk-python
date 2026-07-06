"""Generated from Smithy shape ``com.amazonaws.auditmanager#RegisterAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.account_id
    import aws_sdk_auditmanager.types.kms_key


class RegisterAccountRequest(TypedDict, closed=True):
    kms_key: NotRequired["aws_sdk_auditmanager.types.kms_key.KmsKey"]
    """<p> The KMS key details. </p>"""
    delegated_admin_account: NotRequired[
        "aws_sdk_auditmanager.types.account_id.AccountId"
    ]
    """<p> The delegated administrator account for Audit Manager. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAccountRequest) -> dict:
    out: dict = {}
    if "kms_key" in value:
        out["kmsKey"] = value["kms_key"]
    if "delegated_admin_account" in value:
        out["delegatedAdminAccount"] = value["delegated_admin_account"]
    return out


def deserialize_json(data: dict) -> RegisterAccountRequest:
    out: RegisterAccountRequest = {}  # type: ignore[typeddict-item]
    if "kmsKey" in data:
        out["kms_key"] = data["kmsKey"]
    if "delegatedAdminAccount" in data:
        out["delegated_admin_account"] = data["delegatedAdminAccount"]
    return out
