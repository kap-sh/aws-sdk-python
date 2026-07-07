"""Generated from Smithy shape ``com.amazonaws.glue#CreatePartitionResponse``."""

from typing_extensions import TypedDict


class CreatePartitionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePartitionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePartitionResponse:
    out: CreatePartitionResponse = {}  # type: ignore[typeddict-item]
    return out
