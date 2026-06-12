"""Generated from Smithy shape ``com.amazonaws.guardduty#Account``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class Account(TypedDict):
    uid: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID within which the activity took place. This may differ from the account that owns the user identity.</p>"""
    name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Name of the member's Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Account) -> dict:
    out: dict = {}
    if "uid" in value:
        out["uid"] = value["uid"]
    if "name" in value:
        out["account"] = value["name"]
    return out


def deserialize_json(data: dict) -> Account:
    out: Account = {}  # type: ignore[typeddict-item]
    if "uid" in data:
        out["uid"] = data["uid"]
    if "account" in data:
        out["name"] = data["account"]
    return out
