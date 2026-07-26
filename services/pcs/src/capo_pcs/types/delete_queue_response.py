"""Generated from Smithy shape ``com.amazonaws.pcs#DeleteQueueResponse``."""

from typing_extensions import TypedDict


class DeleteQueueResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteQueueResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteQueueResponse:
    out: DeleteQueueResponse = {}  # type: ignore[typeddict-item]
    return out
