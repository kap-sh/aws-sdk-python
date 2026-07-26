"""Generated from Smithy shape ``com.amazonaws.guardduty#DeleteDetectorResponse``."""

from typing_extensions import TypedDict


class DeleteDetectorResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDetectorResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDetectorResponse:
    out: DeleteDetectorResponse = {}  # type: ignore[typeddict-item]
    return out
