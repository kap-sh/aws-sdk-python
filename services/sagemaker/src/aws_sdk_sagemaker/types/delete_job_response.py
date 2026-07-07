"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteJobResponse``."""

from typing_extensions import TypedDict


class DeleteJobResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteJobResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteJobResponse:
    out: DeleteJobResponse = {}  # type: ignore[typeddict-item]
    return out
