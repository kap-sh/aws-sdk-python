"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeregisterOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.account_id


class DeregisterOrganizationAdminAccountRequest(TypedDict):
    admin_account_id: NotRequired["aws_sdk_auditmanager.types.account_id.AccountId"]
    """<p> The identifier for the administrator account. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    return out


def deserialize_json(data: dict) -> DeregisterOrganizationAdminAccountRequest:
    out: DeregisterOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "adminAccountId" in data:
        out["admin_account_id"] = data["adminAccountId"]
    return out
