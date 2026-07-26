"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CompleteWebAuthnRegistrationResponse``."""

from typing_extensions import TypedDict


class CompleteWebAuthnRegistrationResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompleteWebAuthnRegistrationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CompleteWebAuthnRegistrationResponse:
    out: CompleteWebAuthnRegistrationResponse = {}  # type: ignore[typeddict-item]
    return out
