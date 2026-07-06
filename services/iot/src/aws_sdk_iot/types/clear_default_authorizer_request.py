"""Generated from Smithy shape ``com.amazonaws.iot#ClearDefaultAuthorizerRequest``."""

from typing_extensions import TypedDict


class ClearDefaultAuthorizerRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: ClearDefaultAuthorizerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ClearDefaultAuthorizerRequest:
    out: ClearDefaultAuthorizerRequest = {}  # type: ignore[typeddict-item]
    return out
