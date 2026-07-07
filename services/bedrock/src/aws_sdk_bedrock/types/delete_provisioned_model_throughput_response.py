"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteProvisionedModelThroughputResponse``."""

from typing_extensions import TypedDict


class DeleteProvisionedModelThroughputResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProvisionedModelThroughputResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProvisionedModelThroughputResponse:
    out: DeleteProvisionedModelThroughputResponse = {}  # type: ignore[typeddict-item]
    return out
