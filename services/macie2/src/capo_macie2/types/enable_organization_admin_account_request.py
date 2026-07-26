"""Generated from Smithy shape ``com.amazonaws.macie2#EnableOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class EnableOrganizationAdminAccountRequest(TypedDict, closed=True):
    admin_account_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account to designate as the delegated Amazon Macie administrator account for the organization.</p>"""
    client_token: NotRequired["capo_macie2.types.__string.__string"]
    """<p>A unique, case-sensitive token that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> EnableOrganizationAdminAccountRequest:
    out: EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "adminAccountId" in data:
        out["admin_account_id"] = data["adminAccountId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
