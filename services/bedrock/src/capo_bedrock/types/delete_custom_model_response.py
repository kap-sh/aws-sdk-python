"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteCustomModelResponse``."""

from typing_extensions import TypedDict


class DeleteCustomModelResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomModelResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomModelResponse:
    out: DeleteCustomModelResponse = {}  # type: ignore[typeddict-item]
    return out
