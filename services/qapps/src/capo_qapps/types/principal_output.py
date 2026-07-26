"""Generated from Smithy shape ``com.amazonaws.qapps#PrincipalOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.user_type


class PrincipalOutput(TypedDict, closed=True):
    user_id: NotRequired["str"]
    """<p>The unique identifier of the user.</p>"""
    user_type: NotRequired["capo_qapps.types.user_type.UserType"]
    """<p>The type of the user.</p>"""
    email: NotRequired["str"]
    """<p>The email address associated with the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalOutput) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "user_type" in value:
        import capo_qapps.types.user_type

        out["userType"] = capo_qapps.types.user_type.serialize_json(value["user_type"])
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_json(data: dict) -> PrincipalOutput:
    out: PrincipalOutput = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "userType" in data:
        import capo_qapps.types.user_type

        out["user_type"] = capo_qapps.types.user_type.deserialize_json(data["userType"])
    if "email" in data:
        out["email"] = data["email"]
    return out
