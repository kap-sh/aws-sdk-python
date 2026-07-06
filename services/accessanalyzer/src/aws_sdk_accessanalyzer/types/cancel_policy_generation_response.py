"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CancelPolicyGenerationResponse``."""

from typing_extensions import TypedDict


class CancelPolicyGenerationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelPolicyGenerationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelPolicyGenerationResponse:
    out: CancelPolicyGenerationResponse = {}  # type: ignore[typeddict-item]
    return out
