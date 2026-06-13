"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CodeLine``."""

from typing import TypedDict

from typing_extensions import NotRequired


class CodeLine(TypedDict):
    number: NotRequired["int"]
    """<p>The code line number.</p>"""
    content: NotRequired["str"]
    """<p>The code that contains a vulnerability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeLine) -> dict:
    out: dict = {}
    if "number" in value:
        out["number"] = value["number"]
    if "content" in value:
        out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> CodeLine:
    out: CodeLine = {}  # type: ignore[typeddict-item]
    if "number" in data:
        out["number"] = data["number"]
    if "content" in data:
        out["content"] = data["content"]
    return out
