"""Generated from Smithy shape ``com.amazonaws.iot#ClearDefaultAuthorizerResponse``."""

from typing_extensions import TypedDict


class ClearDefaultAuthorizerResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ClearDefaultAuthorizerResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ClearDefaultAuthorizerResponse:
    out: ClearDefaultAuthorizerResponse = {}  # type: ignore[typeddict-item]
    return out
