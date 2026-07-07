"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminSetUserSettingsResponse``."""

from typing_extensions import TypedDict


class AdminSetUserSettingsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminSetUserSettingsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminSetUserSettingsResponse:
    out: AdminSetUserSettingsResponse = {}  # type: ignore[typeddict-item]
    return out
