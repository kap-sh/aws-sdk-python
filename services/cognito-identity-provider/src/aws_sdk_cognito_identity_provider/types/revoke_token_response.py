"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#RevokeTokenResponse``."""

from typing import TypedDict


class RevokeTokenResponse(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevokeTokenResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RevokeTokenResponse:
    out: RevokeTokenResponse = {}  # type: ignore[typeddict-item]
    return out
