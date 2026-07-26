"""Generated from Smithy shape ``com.amazonaws.lambda#ContextStartedDetails``."""

from typing_extensions import TypedDict


class ContextStartedDetails(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ContextStartedDetails) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ContextStartedDetails:
    out: ContextStartedDetails = {}  # type: ignore[typeddict-item]
    return out
