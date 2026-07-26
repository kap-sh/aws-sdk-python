"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ResumeBatchLoadTaskResponse``."""

from typing_extensions import TypedDict


class ResumeBatchLoadTaskResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResumeBatchLoadTaskResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ResumeBatchLoadTaskResponse:
    out: ResumeBatchLoadTaskResponse = {}  # type: ignore[typeddict-item]
    return out
