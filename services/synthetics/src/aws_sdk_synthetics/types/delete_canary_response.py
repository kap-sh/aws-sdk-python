"""Generated from Smithy shape ``com.amazonaws.synthetics#DeleteCanaryResponse``."""

from typing_extensions import TypedDict


class DeleteCanaryResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCanaryResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCanaryResponse:
    out: DeleteCanaryResponse = {}  # type: ignore[typeddict-item]
    return out
