"""Generated from Smithy shape ``com.amazonaws.connect#DeleteEmailAddressResponse``."""

from typing_extensions import TypedDict


class DeleteEmailAddressResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailAddressResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEmailAddressResponse:
    out: DeleteEmailAddressResponse = {}  # type: ignore[typeddict-item]
    return out
