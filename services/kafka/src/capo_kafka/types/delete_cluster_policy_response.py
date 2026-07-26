"""Generated from Smithy shape ``com.amazonaws.kafka#DeleteClusterPolicyResponse``."""

from typing_extensions import TypedDict


class DeleteClusterPolicyResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterPolicyResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterPolicyResponse:
    out: DeleteClusterPolicyResponse = {}  # type: ignore[typeddict-item]
    return out
