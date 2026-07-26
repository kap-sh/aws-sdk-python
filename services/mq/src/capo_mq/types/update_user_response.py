"""Generated from Smithy shape ``com.amazonaws.mq#UpdateUserResponse``."""

from typing_extensions import TypedDict


class UpdateUserResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UpdateUserResponse:
    out: UpdateUserResponse = {}  # type: ignore[typeddict-item]
    return out
