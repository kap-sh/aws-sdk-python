"""Generated from Smithy shape ``com.amazonaws.ecr#GetSigningConfigurationRequest``."""

from typing_extensions import TypedDict


class GetSigningConfigurationRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSigningConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSigningConfigurationRequest:
    out: GetSigningConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
