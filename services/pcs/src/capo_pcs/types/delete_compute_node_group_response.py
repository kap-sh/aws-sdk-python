"""Generated from Smithy shape ``com.amazonaws.pcs#DeleteComputeNodeGroupResponse``."""

from typing_extensions import TypedDict


class DeleteComputeNodeGroupResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteComputeNodeGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteComputeNodeGroupResponse:
    out: DeleteComputeNodeGroupResponse = {}  # type: ignore[typeddict-item]
    return out
