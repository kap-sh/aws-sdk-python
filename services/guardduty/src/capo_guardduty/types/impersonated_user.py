"""Generated from Smithy shape ``com.amazonaws.guardduty#ImpersonatedUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.groups
    import capo_guardduty.types.string


class ImpersonatedUser(TypedDict, closed=True):
    username: NotRequired["capo_guardduty.types.string.String"]
    """<p>Information about the <code>username</code> that was being impersonated.</p>"""
    groups: NotRequired["capo_guardduty.types.groups.Groups"]
    """<p>The <code>group</code> to which the user name belongs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImpersonatedUser) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "groups" in value:
        import capo_guardduty.types.groups

        out["groups"] = capo_guardduty.types.groups.serialize_json(value["groups"])
    return out


def deserialize_json(data: dict) -> ImpersonatedUser:
    out: ImpersonatedUser = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    if "groups" in data:
        import capo_guardduty.types.groups

        out["groups"] = capo_guardduty.types.groups.deserialize_json(data["groups"])
    return out
