"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Hash``."""

from typing_extensions import NotRequired, TypedDict


class Hash(TypedDict, closed=True):
    sha256: NotRequired["str"]
    """<p> The SHA-256 hash value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Hash) -> dict:
    out: dict = {}
    if "sha256" in value:
        out["sha256"] = value["sha256"]
    return out


def deserialize_json(data: dict) -> Hash:
    out: Hash = {}  # type: ignore[typeddict-item]
    if "sha256" in data:
        out["sha256"] = data["sha256"]
    return out
