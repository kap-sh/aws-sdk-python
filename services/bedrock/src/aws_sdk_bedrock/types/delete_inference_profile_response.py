"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteInferenceProfileResponse``."""

from typing_extensions import TypedDict


class DeleteInferenceProfileResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInferenceProfileResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInferenceProfileResponse:
    out: DeleteInferenceProfileResponse = {}  # type: ignore[typeddict-item]
    return out
