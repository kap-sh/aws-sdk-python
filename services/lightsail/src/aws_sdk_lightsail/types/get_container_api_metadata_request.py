"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerAPIMetadataRequest``."""

from typing_extensions import TypedDict


class GetContainerAPIMetadataRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerAPIMetadataRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerAPIMetadataRequest:
    out: GetContainerAPIMetadataRequest = {}  # type: ignore[typeddict-item]
    return out
