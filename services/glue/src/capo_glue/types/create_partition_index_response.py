"""Generated from Smithy shape ``com.amazonaws.glue#CreatePartitionIndexResponse``."""

from typing_extensions import TypedDict


class CreatePartitionIndexResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartitionIndexResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartitionIndexResponse:
    out: CreatePartitionIndexResponse = {}  # type: ignore[typeddict-item]
    return out
