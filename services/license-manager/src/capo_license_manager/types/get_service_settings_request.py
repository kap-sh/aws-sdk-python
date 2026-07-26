"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetServiceSettingsRequest``."""

from typing_extensions import TypedDict


class GetServiceSettingsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetServiceSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetServiceSettingsRequest:
    out: GetServiceSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
