"""Generated from Smithy shape ``com.amazonaws.auditmanager#GetOrganizationAdminAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.account_id
    import capo_auditmanager.types.organization_id


class GetOrganizationAdminAccountResponse(TypedDict, closed=True):
    admin_account_id: NotRequired["capo_auditmanager.types.account_id.AccountId"]
    """<p> The identifier for the administrator account. </p>"""
    organization_id: NotRequired[
        "capo_auditmanager.types.organization_id.organizationId"
    ]
    """<p> The identifier for the organization. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOrganizationAdminAccountResponse) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    return out


def deserialize_json(data: dict) -> GetOrganizationAdminAccountResponse:
    out: GetOrganizationAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if "adminAccountId" in data:
        out["admin_account_id"] = data["adminAccountId"]
    if "organizationId" in data:
        out["organization_id"] = data["organizationId"]
    return out
