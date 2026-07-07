"""Generated from Smithy shape ``com.amazonaws.glue#DeletePartitionResponse``."""

from typing_extensions import TypedDict


class DeletePartitionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePartitionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePartitionResponse:
    out: DeletePartitionResponse = {}  # type: ignore[typeddict-item]
    return out
