"""Generated from Smithy shape ``com.amazonaws.sesv2#DeleteContactResponse``."""

from typing_extensions import TypedDict


class DeleteContactResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteContactResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteContactResponse:
    out: DeleteContactResponse = {}  # type: ignore[typeddict-item]
    return out
