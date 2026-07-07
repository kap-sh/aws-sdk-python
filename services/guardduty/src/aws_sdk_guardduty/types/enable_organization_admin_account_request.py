"""Generated from Smithy shape ``com.amazonaws.guardduty#EnableOrganizationAdminAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class EnableOrganizationAdminAccountRequest(TypedDict, closed=True):
    admin_account_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID for the organization account to be enabled as a GuardDuty delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableOrganizationAdminAccountRequest) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    return out


def deserialize_json(data: dict) -> EnableOrganizationAdminAccountRequest:
    out: EnableOrganizationAdminAccountRequest = {}  # type: ignore[typeddict-item]
    if "adminAccountId" in data:
        out["admin_account_id"] = data["adminAccountId"]
    return out
