"""Generated from Smithy shape ``com.amazonaws.ssm#AccountSharingInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.account_id
    import capo_ssm.types.shared_document_version


class AccountSharingInfo(TypedDict, closed=True):
    account_id: NotRequired["capo_ssm.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID where the current document is shared.</p>"""
    shared_document_version: NotRequired[
        "capo_ssm.types.shared_document_version.SharedDocumentVersion"
    ]
    """<p>The version of the current document shared with the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountSharingInfo) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "shared_document_version" in value:
        out["SharedDocumentVersion"] = value["shared_document_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountSharingInfo:
    out: AccountSharingInfo = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "SharedDocumentVersion" in data:
        out["shared_document_version"] = data["SharedDocumentVersion"]
    return out
