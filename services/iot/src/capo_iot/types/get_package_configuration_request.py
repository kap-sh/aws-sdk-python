"""Generated from Smithy shape ``com.amazonaws.iot#GetPackageConfigurationRequest``."""

from typing_extensions import TypedDict


class GetPackageConfigurationRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetPackageConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPackageConfigurationRequest:
    out: GetPackageConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
