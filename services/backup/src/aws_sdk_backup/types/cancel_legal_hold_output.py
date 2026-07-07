"""Generated from Smithy shape ``com.amazonaws.backup#CancelLegalHoldOutput``."""

from typing_extensions import TypedDict


class CancelLegalHoldOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelLegalHoldOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelLegalHoldOutput:
    out: CancelLegalHoldOutput = {}  # type: ignore[typeddict-item]
    return out
