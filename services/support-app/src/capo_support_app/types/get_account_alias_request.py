"""Generated from Smithy shape ``com.amazonaws.supportapp#GetAccountAliasRequest``."""

from typing_extensions import TypedDict


class GetAccountAliasRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountAliasRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountAliasRequest:
    out: GetAccountAliasRequest = {}  # type: ignore[typeddict-item]
    return out
