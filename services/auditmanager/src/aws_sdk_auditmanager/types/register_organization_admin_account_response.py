"""Generated from Smithy shape ``com.amazonaws.auditmanager#RegisterOrganizationAdminAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.account_id
    import aws_sdk_auditmanager.types.organization_id


class RegisterOrganizationAdminAccountResponse(TypedDict):
    admin_account_id: NotRequired["aws_sdk_auditmanager.types.account_id.AccountId"]
    """<p> The identifier for the delegated administrator account. </p>"""
    organization_id: NotRequired[
        "aws_sdk_auditmanager.types.organization_id.organizationId"
    ]
    """<p> The identifier for the organization. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOrganizationAdminAccountResponse) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    if "organization_id" in value:
        out["organizationId"] = value["organization_id"]
    return out


def deserialize_json(data: dict) -> RegisterOrganizationAdminAccountResponse:
    out: RegisterOrganizationAdminAccountResponse = {}  # type: ignore[typeddict-item]
    if "adminAccountId" in data:
        out["admin_account_id"] = data["adminAccountId"]
    if "organizationId" in data:
        out["organization_id"] = data["organizationId"]
    return out
