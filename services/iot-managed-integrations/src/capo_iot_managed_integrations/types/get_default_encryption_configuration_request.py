"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetDefaultEncryptionConfigurationRequest``."""

from typing_extensions import TypedDict


class GetDefaultEncryptionConfigurationRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetDefaultEncryptionConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDefaultEncryptionConfigurationRequest:
    out: GetDefaultEncryptionConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
