"""Generated from Smithy shape ``com.amazonaws.guardduty#AdminAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.admin_status
    import capo_guardduty.types.string


class AdminAccount(TypedDict, closed=True):
    admin_account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID for the account.</p>"""
    admin_status: NotRequired["capo_guardduty.types.admin_status.AdminStatus"]
    """<p>Indicates whether the account is enabled as the delegated administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccount) -> dict:
    out: dict = {}
    if "admin_account_id" in value:
        out["adminAccountId"] = value["admin_account_id"]
    if "admin_status" in value:
        import capo_guardduty.types.admin_status

        out["adminStatus"] = capo_guardduty.types.admin_status.serialize_json(
            value["admin_status"]
        )
    return out


def deserialize_json(data: dict) -> AdminAccount:
    out: AdminAccount = {}  # type: ignore[typeddict-item]
    if "adminAccountId" in data:
        out["admin_account_id"] = data["adminAccountId"]
    if "adminStatus" in data:
        import capo_guardduty.types.admin_status

        out["admin_status"] = capo_guardduty.types.admin_status.deserialize_json(
            data["adminStatus"]
        )
    return out
