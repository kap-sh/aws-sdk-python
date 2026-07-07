"""Generated from Smithy shape ``com.amazonaws.guardduty#DeletePublishingDestinationResponse``."""

from typing_extensions import TypedDict


class DeletePublishingDestinationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeletePublishingDestinationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePublishingDestinationResponse:
    out: DeletePublishingDestinationResponse = {}  # type: ignore[typeddict-item]
    return out
