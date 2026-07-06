"""Generated from Smithy shape ``com.amazonaws.chime#SigninDelegateGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class SigninDelegateGroup(TypedDict, closed=True):
    group_name: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The group name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SigninDelegateGroup) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    return out


def deserialize_json(data: dict) -> SigninDelegateGroup:
    out: SigninDelegateGroup = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    return out
