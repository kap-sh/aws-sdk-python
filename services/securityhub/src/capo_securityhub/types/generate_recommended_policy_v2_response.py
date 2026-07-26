"""Generated from Smithy shape ``com.amazonaws.securityhub#GenerateRecommendedPolicyV2Response``."""

from typing_extensions import TypedDict


class GenerateRecommendedPolicyV2Response(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GenerateRecommendedPolicyV2Response) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GenerateRecommendedPolicyV2Response:
    out: GenerateRecommendedPolicyV2Response = {}  # type: ignore[typeddict-item]
    return out
