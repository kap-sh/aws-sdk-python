"""Generated from Smithy shape ``com.amazonaws.devicefarm#GetAccountSettingsRequest``."""

from typing_extensions import TypedDict


class GetAccountSettingsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountSettingsRequest:
    out: GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
