"""Generated from Smithy shape ``com.amazonaws.securityhub#DisableSecurityHubV2Response``."""

from typing_extensions import TypedDict


class DisableSecurityHubV2Response(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisableSecurityHubV2Response) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisableSecurityHubV2Response:
    out: DisableSecurityHubV2Response = {}  # type: ignore[typeddict-item]
    return out
