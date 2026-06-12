"""Generated from Smithy shape ``com.amazonaws.macie2#AdminAccount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.admin_status


class AdminAccount(TypedDict):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services account ID for the account.</p>"""
    status: NotRequired["aws_sdk_macie2.types.admin_status.AdminStatus"]
    """<p>The current status of the account as the delegated Amazon Macie administrator account for the organization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "status" in value:
        import aws_sdk_macie2.types.admin_status

        out["status"] = aws_sdk_macie2.types.admin_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> AdminAccount:
    out: AdminAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "status" in data:
        import aws_sdk_macie2.types.admin_status

        out["status"] = aws_sdk_macie2.types.admin_status.deserialize_json(
            data["status"]
        )
    return out
