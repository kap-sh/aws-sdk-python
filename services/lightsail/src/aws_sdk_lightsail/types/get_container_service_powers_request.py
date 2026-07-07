"""Generated from Smithy shape ``com.amazonaws.lightsail#GetContainerServicePowersRequest``."""

from typing_extensions import TypedDict


class GetContainerServicePowersRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContainerServicePowersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContainerServicePowersRequest:
    out: GetContainerServicePowersRequest = {}  # type: ignore[typeddict-item]
    return out
