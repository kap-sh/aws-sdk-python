"""Generated from Smithy shape ``com.amazonaws.bedrock#LegalTerm``."""

from typing import TypedDict

from typing_extensions import NotRequired


class LegalTerm(TypedDict):
    url: NotRequired["str"]
    """<p>URL to the legal term document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LegalTerm) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> LegalTerm:
    out: LegalTerm = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out
