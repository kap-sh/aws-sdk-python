"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#GetAccountSettingsRequest``."""

from typing_extensions import TypedDict


class GetAccountSettingsRequest(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountSettingsRequest:
    out: GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
