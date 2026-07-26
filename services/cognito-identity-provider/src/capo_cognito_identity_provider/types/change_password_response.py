"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChangePasswordResponse``."""

from typing_extensions import TypedDict


class ChangePasswordResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChangePasswordResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ChangePasswordResponse:
    out: ChangePasswordResponse = {}  # type: ignore[typeddict-item]
    return out
