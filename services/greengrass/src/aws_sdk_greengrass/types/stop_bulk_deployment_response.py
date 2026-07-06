"""Generated from Smithy shape ``com.amazonaws.greengrass#StopBulkDeploymentResponse``."""

from typing_extensions import TypedDict


class StopBulkDeploymentResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopBulkDeploymentResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopBulkDeploymentResponse:
    out: StopBulkDeploymentResponse = {}  # type: ignore[typeddict-item]
    return out
