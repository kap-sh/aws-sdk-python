"""Generated from Smithy shape ``com.amazonaws.connect#DismissUserContactResponse``."""

from typing_extensions import TypedDict


class DismissUserContactResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DismissUserContactResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DismissUserContactResponse:
    out: DismissUserContactResponse = {}  # type: ignore[typeddict-item]
    return out
