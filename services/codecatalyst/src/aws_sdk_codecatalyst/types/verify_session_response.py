"""Generated from Smithy shape ``com.amazonaws.codecatalyst#VerifySessionResponse``."""

from typing_extensions import NotRequired, TypedDict


class VerifySessionResponse(TypedDict, closed=True):
    identity: NotRequired["str"]
    """<p>The system-generated unique ID of the user in Amazon CodeCatalyst.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifySessionResponse) -> dict:
    out: dict = {}
    if "identity" in value:
        out["identity"] = value["identity"]
    return out


def deserialize_json(data: dict) -> VerifySessionResponse:
    out: VerifySessionResponse = {}  # type: ignore[typeddict-item]
    if "identity" in data:
        out["identity"] = data["identity"]
    return out
