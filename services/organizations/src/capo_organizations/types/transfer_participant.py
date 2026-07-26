"""Generated from Smithy shape ``com.amazonaws.organizations#TransferParticipant``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.account_id
    import capo_organizations.types.email


class TransferParticipant(TypedDict, closed=True):
    management_account_id: NotRequired["capo_organizations.types.account_id.AccountId"]
    """<p>ID for the management account.</p>"""
    management_account_email: NotRequired["capo_organizations.types.email.Email"]
    """<p>Email address for the management account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransferParticipant) -> dict:
    out: dict = {}
    if "management_account_id" in value:
        out["ManagementAccountId"] = value["management_account_id"]
    if "management_account_email" in value:
        out["ManagementAccountEmail"] = value["management_account_email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TransferParticipant:
    out: TransferParticipant = {}  # type: ignore[typeddict-item]
    if "ManagementAccountId" in data:
        out["management_account_id"] = data["ManagementAccountId"]
    if "ManagementAccountEmail" in data:
        out["management_account_email"] = data["ManagementAccountEmail"]
    return out
