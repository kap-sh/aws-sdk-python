"""Generated from Smithy shape ``com.amazonaws.appfabric#DeleteIngestionResponse``."""

from typing_extensions import TypedDict


class DeleteIngestionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIngestionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIngestionResponse:
    out: DeleteIngestionResponse = {}  # type: ignore[typeddict-item]
    return out
