"""Generated from Smithy shape ``com.amazonaws.ecrpublic#GetAuthorizationTokenRequest``."""

from typing import TypedDict


class GetAuthorizationTokenRequest(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAuthorizationTokenRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAuthorizationTokenRequest:
    out: GetAuthorizationTokenRequest = {}  # type: ignore[typeddict-item]
    return out
