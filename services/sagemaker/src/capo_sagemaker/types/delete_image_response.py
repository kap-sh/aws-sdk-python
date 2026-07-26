"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteImageResponse``."""

from typing_extensions import TypedDict


class DeleteImageResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteImageResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteImageResponse:
    out: DeleteImageResponse = {}  # type: ignore[typeddict-item]
    return out
