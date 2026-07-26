"""Generated from Smithy shape ``com.amazonaws.securityhub#AdminAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.admin_status
    import capo_securityhub.types.non_empty_string


class AdminAccount(TypedDict, closed=True):
    account_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account identifier of the Security Hub CSPM administrator account.</p>"""
    status: NotRequired["capo_securityhub.types.admin_status.AdminStatus"]
    """<p>The current status of the Security Hub CSPM administrator account. Indicates whether the account is currently enabled as a Security Hub CSPM administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "status" in value:
        import capo_securityhub.types.admin_status

        out["Status"] = capo_securityhub.types.admin_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> AdminAccount:
    out: AdminAccount = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Status" in data:
        import capo_securityhub.types.admin_status

        out["status"] = capo_securityhub.types.admin_status.deserialize_json(
            data["Status"]
        )
    return out
