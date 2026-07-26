"""Generated from Smithy shape ``com.amazonaws.iot#DescribeEncryptionConfigurationRequest``."""

from typing_extensions import TypedDict


class DescribeEncryptionConfigurationRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEncryptionConfigurationRequest:
    out: DescribeEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
