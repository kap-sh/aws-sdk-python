"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#VerifyUserAttributeResponse``."""

from typing_extensions import TypedDict


class VerifyUserAttributeResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VerifyUserAttributeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> VerifyUserAttributeResponse:
    out: VerifyUserAttributeResponse = {}  # type: ignore[typeddict-item]
    return out
