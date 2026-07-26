"""Generated from Smithy shape ``com.amazonaws.guardduty#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account
    import capo_guardduty.types.string


class User(TypedDict, closed=True):
    name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the user.</p>"""
    uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique identifier of the user.</p>"""
    type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the user.</p>"""
    credential_uid: NotRequired["capo_guardduty.types.string.String"]
    """<p>The credentials of the user ID.</p>"""
    account: NotRequired["capo_guardduty.types.account.Account"]
    """<p>Contains information about the Amazon Web Services account within which the activity took place. This is not necessarily the account that owns the user identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "uid" in value:
        out["uid"] = value["uid"]
    if "type" in value:
        out["type"] = value["type"]
    if "credential_uid" in value:
        out["credentialUid"] = value["credential_uid"]
    if "account" in value:
        import capo_guardduty.types.account

        out["account"] = capo_guardduty.types.account.serialize_json(value["account"])
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "type" in data:
        out["type"] = data["type"]
    if "credentialUid" in data:
        out["credential_uid"] = data["credentialUid"]
    if "account" in data:
        import capo_guardduty.types.account

        out["account"] = capo_guardduty.types.account.deserialize_json(data["account"])
    return out
