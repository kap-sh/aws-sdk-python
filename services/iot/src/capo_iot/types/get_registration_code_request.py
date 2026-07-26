"""Generated from Smithy shape ``com.amazonaws.iot#GetRegistrationCodeRequest``."""

from typing_extensions import TypedDict


class GetRegistrationCodeRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetRegistrationCodeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRegistrationCodeRequest:
    out: GetRegistrationCodeRequest = {}  # type: ignore[typeddict-item]
    return out
