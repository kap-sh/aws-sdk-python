"""Generated from Smithy shape ``com.amazonaws.securityhub#DisableSecurityHubV2Request``."""

from typing_extensions import TypedDict


class DisableSecurityHubV2Request(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisableSecurityHubV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableSecurityHubV2Request:
    out: DisableSecurityHubV2Request = {}  # type: ignore[typeddict-item]
    return out
