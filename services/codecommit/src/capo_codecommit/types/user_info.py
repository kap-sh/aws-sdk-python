"""Generated from Smithy shape ``com.amazonaws.codecommit#UserInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.date
    import capo_codecommit.types.email
    import capo_codecommit.types.name


class UserInfo(TypedDict, closed=True):
    name: NotRequired["capo_codecommit.types.name.Name"]
    """<p>The name of the user who made the specified commit.</p>"""
    email: NotRequired["capo_codecommit.types.email.Email"]
    """<p>The email address associated with the user who made the commit, if any.</p>"""
    date: NotRequired["capo_codecommit.types.date.Date"]
    """<p>The date when the specified commit was commited, in timestamp format with GMT offset.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    if "date" in value:
        out["date"] = value["date"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserInfo:
    out: UserInfo = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "email" in data:
        out["email"] = data["email"]
    if "date" in data:
        out["date"] = data["date"]
    return out
