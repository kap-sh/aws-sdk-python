"""Generated from Smithy shape ``com.amazonaws.odb#GetOciOnboardingStatusInput``."""

from typing_extensions import TypedDict


class GetOciOnboardingStatusInput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetOciOnboardingStatusInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetOciOnboardingStatusInput:
    out: GetOciOnboardingStatusInput = {}  # type: ignore[typeddict-item]
    return out
