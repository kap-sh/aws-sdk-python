"""Generated from Smithy shape ``com.amazonaws.proton#GetAccountSettingsInput``."""

from typing_extensions import TypedDict


class GetAccountSettingsInput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAccountSettingsInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAccountSettingsInput:
    out: GetAccountSettingsInput = {}  # type: ignore[typeddict-item]
    return out
