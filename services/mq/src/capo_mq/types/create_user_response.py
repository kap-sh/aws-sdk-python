"""Generated from Smithy shape ``com.amazonaws.mq#CreateUserResponse``."""

from typing_extensions import TypedDict


class CreateUserResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateUserResponse:
    out: CreateUserResponse = {}  # type: ignore[typeddict-item]
    return out
