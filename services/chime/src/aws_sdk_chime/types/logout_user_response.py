"""Generated from Smithy shape ``com.amazonaws.chime#LogoutUserResponse``."""

from typing import TypedDict


class LogoutUserResponse(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: LogoutUserResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> LogoutUserResponse:
    out: LogoutUserResponse = {}  # type: ignore[typeddict-item]
    return out
