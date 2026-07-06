"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetEncryptionConfigurationRequest``."""

from typing_extensions import TypedDict


class GetEncryptionConfigurationRequest(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEncryptionConfigurationRequest:
    out: GetEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
