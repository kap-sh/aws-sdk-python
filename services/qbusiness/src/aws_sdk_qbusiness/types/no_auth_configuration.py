"""Generated from Smithy shape ``com.amazonaws.qbusiness#NoAuthConfiguration``."""

from typing_extensions import TypedDict


class NoAuthConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: NoAuthConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> NoAuthConfiguration:
    out: NoAuthConfiguration = {}  # type: ignore[typeddict-item]
    return out
