"""Generated from Smithy shape ``com.amazonaws.glue#DeletePartitionIndexResponse``."""

from typing_extensions import TypedDict


class DeletePartitionIndexResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePartitionIndexResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePartitionIndexResponse:
    out: DeletePartitionIndexResponse = {}  # type: ignore[typeddict-item]
    return out
