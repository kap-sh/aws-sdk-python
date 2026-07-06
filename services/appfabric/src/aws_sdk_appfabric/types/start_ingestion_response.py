"""Generated from Smithy shape ``com.amazonaws.appfabric#StartIngestionResponse``."""

from typing_extensions import TypedDict


class StartIngestionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StartIngestionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartIngestionResponse:
    out: StartIngestionResponse = {}  # type: ignore[typeddict-item]
    return out
