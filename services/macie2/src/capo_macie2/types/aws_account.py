"""Generated from Smithy shape ``com.amazonaws.macie2#AwsAccount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__string


class AwsAccount(TypedDict, closed=True):
    account_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account.</p>"""
    principal_id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the entity that performed the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAccount) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "principal_id" in value:
        out["principalId"] = value["principal_id"]
    return out


def deserialize_json(data: dict) -> AwsAccount:
    out: AwsAccount = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "principalId" in data:
        out["principal_id"] = data["principalId"]
    return out
