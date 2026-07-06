"""Generated from Smithy shape ``com.amazonaws.rekognition#StopStreamProcessorResponse``."""

from typing_extensions import TypedDict


class StopStreamProcessorResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopStreamProcessorResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> StopStreamProcessorResponse:
    out: StopStreamProcessorResponse = {}  # type: ignore[typeddict-item]
    return out
