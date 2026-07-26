"""Generated from Smithy shape ``com.amazonaws.securityhub#DisableSecurityHubRequest``."""

from typing_extensions import TypedDict


class DisableSecurityHubRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisableSecurityHubRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableSecurityHubRequest:
    out: DisableSecurityHubRequest = {}  # type: ignore[typeddict-item]
    return out
