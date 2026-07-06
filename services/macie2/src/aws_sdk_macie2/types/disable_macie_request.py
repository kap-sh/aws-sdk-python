"""Generated from Smithy shape ``com.amazonaws.macie2#DisableMacieRequest``."""

from typing_extensions import TypedDict


class DisableMacieRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisableMacieRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableMacieRequest:
    out: DisableMacieRequest = {}  # type: ignore[typeddict-item]
    return out
