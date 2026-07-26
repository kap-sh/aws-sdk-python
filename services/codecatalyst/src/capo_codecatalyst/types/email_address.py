"""Generated from Smithy shape ``com.amazonaws.codecatalyst#EmailAddress``."""

from typing_extensions import NotRequired, TypedDict


class EmailAddress(TypedDict, closed=True):
    email: NotRequired["str"]
    """<p>The email address.</p>"""
    verified: NotRequired["bool"]
    """<p>Whether the email address has been verified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddress) -> dict:
    out: dict = {}
    if "email" in value:
        out["email"] = value["email"]
    if "verified" in value:
        out["verified"] = value["verified"]
    return out


def deserialize_json(data: dict) -> EmailAddress:
    out: EmailAddress = {}  # type: ignore[typeddict-item]
    if "email" in data:
        out["email"] = data["email"]
    if "verified" in data:
        out["verified"] = data["verified"]
    return out
