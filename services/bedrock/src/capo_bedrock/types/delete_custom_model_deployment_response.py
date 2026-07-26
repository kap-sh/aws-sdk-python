"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteCustomModelDeploymentResponse``."""

from typing_extensions import TypedDict


class DeleteCustomModelDeploymentResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomModelDeploymentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomModelDeploymentResponse:
    out: DeleteCustomModelDeploymentResponse = {}  # type: ignore[typeddict-item]
    return out
