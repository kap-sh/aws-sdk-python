"""Generated from Smithy shape ``com.amazonaws.polly#PutLexiconOutput``."""

from typing_extensions import TypedDict


class PutLexiconOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutLexiconOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutLexiconOutput:
    out: PutLexiconOutput = {}  # type: ignore[typeddict-item]
    return out
