"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminSetUserMFAPreferenceResponse``."""

from typing_extensions import TypedDict


class AdminSetUserMFAPreferenceResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminSetUserMFAPreferenceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminSetUserMFAPreferenceResponse:
    out: AdminSetUserMFAPreferenceResponse = {}  # type: ignore[typeddict-item]
    return out
