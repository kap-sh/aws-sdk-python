"""Generated from Smithy shape ``com.amazonaws.synthetics#StartCanaryResponse``."""

from typing_extensions import TypedDict


class StartCanaryResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StartCanaryResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartCanaryResponse:
    out: StartCanaryResponse = {}  # type: ignore[typeddict-item]
    return out
