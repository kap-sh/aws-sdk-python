"""Generated from Smithy shape ``com.amazonaws.macie2#AdminAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string
    import capo_macie2.types.admin_status


class AdminAccount(TypedDict, closed=True):
    account_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account.</p>"""
    status: NotRequired["capo_macie2.types.admin_status.AdminStatus"]
    """<p>The current status of the account as the delegated Amazon Macie administrator account for the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        import capo_macie2.types.admin_status

        out["status"] = capo_macie2.types.admin_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> AdminAccount:
    out: AdminAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "status" in data:
        import capo_macie2.types.admin_status

        out["status"] = capo_macie2.types.admin_status.deserialize_json(data["status"])
    return out
