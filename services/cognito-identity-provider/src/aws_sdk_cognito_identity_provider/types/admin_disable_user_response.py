"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminDisableUserResponse``."""

from typing_extensions import TypedDict


class AdminDisableUserResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminDisableUserResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminDisableUserResponse:
    out: AdminDisableUserResponse = {}  # type: ignore[typeddict-item]
    return out
