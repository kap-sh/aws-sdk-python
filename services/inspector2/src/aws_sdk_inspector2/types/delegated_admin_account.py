"""Generated from Smithy shape ``com.amazonaws.inspector2#DelegatedAdminAccount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.delegated_admin_status


class DelegatedAdminAccount(TypedDict):
    account_id: NotRequired["aws_sdk_inspector2.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the Amazon Inspector delegated administrator for your organization.</p>"""
    status: NotRequired[
        "aws_sdk_inspector2.types.delegated_admin_status.DelegatedAdminStatus"
    ]
    """<p>The status of the Amazon Inspector delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DelegatedAdminAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_json(data: dict) -> DelegatedAdminAccount:
    out: DelegatedAdminAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "status" in data:
        out["status"] = data["status"]
    return out
