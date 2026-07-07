"""Generated from Smithy shape ``com.amazonaws.securityhub#DisableSecurityHubResponse``."""

from typing_extensions import TypedDict


class DisableSecurityHubResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisableSecurityHubResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableSecurityHubResponse:
    out: DisableSecurityHubResponse = {}  # type: ignore[typeddict-item]
    return out
