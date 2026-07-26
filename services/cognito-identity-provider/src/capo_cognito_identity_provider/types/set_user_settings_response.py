"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SetUserSettingsResponse``."""

from typing_extensions import TypedDict


class SetUserSettingsResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetUserSettingsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> SetUserSettingsResponse:
    out: SetUserSettingsResponse = {}  # type: ignore[typeddict-item]
    return out
