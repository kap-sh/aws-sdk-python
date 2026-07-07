"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#SendEmailVerificationCodeResponse``."""

from typing_extensions import TypedDict


class SendEmailVerificationCodeResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SendEmailVerificationCodeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> SendEmailVerificationCodeResponse:
    out: SendEmailVerificationCodeResponse = {}  # type: ignore[typeddict-item]
    return out
