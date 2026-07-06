"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAccountDataRetentionRequest``."""

from typing_extensions import TypedDict


class GetAccountDataRetentionRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountDataRetentionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountDataRetentionRequest:
    out: GetAccountDataRetentionRequest = {}  # type: ignore[typeddict-item]
    return out
