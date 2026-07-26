"""Generated from Smithy shape ``com.amazonaws.guardduty#DisableOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class DisableOrganizationAdminAccountRequest(TypedDict, closed=True):
    admin_account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services Account ID for the organizations account to be disabled as a GuardDuty delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisableOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    return out


def deserialize_json(data: dict) -> DisableOrganizationAdminAccountRequest:
    out: DisableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "adminAccountId" in data:
        out["admin_account_id"] = data["adminAccountId"]
    return out
