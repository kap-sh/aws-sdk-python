"""Generated from Smithy shape ``com.amazonaws.securityhub#AdminAccount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.admin_status
    import aws_sdk_securityhub.types.non_empty_string


class AdminAccount(TypedDict):
    account_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Web Services account identifier of the Security Hub CSPM administrator account.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.admin_status.AdminStatus"]
    """<p>The current status of the Security Hub CSPM administrator account. Indicates whether the account is currently enabled as a Security Hub CSPM administrator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdminAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "status" in value:
        import aws_sdk_securityhub.types.admin_status

        out["Status"] = aws_sdk_securityhub.types.admin_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> AdminAccount:
    out: AdminAccount = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "Status" in data:
        import aws_sdk_securityhub.types.admin_status

        out["status"] = aws_sdk_securityhub.types.admin_status.deserialize_json(
            data["Status"]
        )
    return out
