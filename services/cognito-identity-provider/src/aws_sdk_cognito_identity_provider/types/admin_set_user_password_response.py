"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminSetUserPasswordResponse``."""

from typing_extensions import TypedDict


class AdminSetUserPasswordResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminSetUserPasswordResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminSetUserPasswordResponse:
    out: AdminSetUserPasswordResponse = {}  # type: ignore[typeddict-item]
    return out
