"""Generated from Smithy shape ``com.amazonaws.detective#NewUserAgentDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.is_new_for_entire_account
    import aws_sdk_detective.types.user_agent


class NewUserAgentDetail(TypedDict, closed=True):
    user_agent: NotRequired["aws_sdk_detective.types.user_agent.UserAgent"]
    """<p>New user agent which accessed the resource.</p>"""
    is_new_for_entire_account: (
        "aws_sdk_detective.types.is_new_for_entire_account.IsNewForEntireAccount"
    )
    """<p>Checks if the user agent is new for the entire account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NewUserAgentDetail) -> dict:
    out: dict = {}
    if "user_agent" in value:
        out["UserAgent"] = value["user_agent"]
    out["IsNewForEntireAccount"] = value.get("is_new_for_entire_account", False)
    return out


def deserialize_json(data: dict) -> NewUserAgentDetail:
    out: NewUserAgentDetail = {}  # type: ignore[typeddict-item]
    if "UserAgent" in data:
        out["user_agent"] = data["UserAgent"]
    if "IsNewForEntireAccount" in data:
        out["is_new_for_entire_account"] = data["IsNewForEntireAccount"]
    else:
        out["is_new_for_entire_account"] = False
    return out
