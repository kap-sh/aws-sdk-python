"""Generated from Smithy shape ``com.amazonaws.wickr#PasswordRequirements``."""

from typing_extensions import NotRequired, TypedDict


class PasswordRequirements(TypedDict, closed=True):
    lowercase: NotRequired["int"]
    """<p>The minimum number of lowercase letters required in passwords.</p>"""
    min_length: NotRequired["int"]
    """<p>The minimum password length in characters.</p>"""
    numbers: NotRequired["int"]
    """<p>The minimum number of numeric characters required in passwords.</p>"""
    symbols: NotRequired["int"]
    """<p>The minimum number of special symbol characters required in passwords.</p>"""
    uppercase: NotRequired["int"]
    """<p>The minimum number of uppercase letters required in passwords.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PasswordRequirements) -> dict:
    out: dict = {}
    if "lowercase" in value:
        out["lowercase"] = value["lowercase"]
    if "min_length" in value:
        out["minLength"] = value["min_length"]
    if "numbers" in value:
        out["numbers"] = value["numbers"]
    if "symbols" in value:
        out["symbols"] = value["symbols"]
    if "uppercase" in value:
        out["uppercase"] = value["uppercase"]
    return out


def deserialize_json(data: dict) -> PasswordRequirements:
    out: PasswordRequirements = {}  # type: ignore[typeddict-item]
    if "lowercase" in data:
        out["lowercase"] = data["lowercase"]
    if "minLength" in data:
        out["min_length"] = data["minLength"]
    if "numbers" in data:
        out["numbers"] = data["numbers"]
    if "symbols" in data:
        out["symbols"] = data["symbols"]
    if "uppercase" in data:
        out["uppercase"] = data["uppercase"]
    return out
