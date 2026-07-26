"""Generated from Smithy shape ``com.amazonaws.macie2#GetAutomatedDiscoveryConfigurationRequest``."""

from typing_extensions import TypedDict


class GetAutomatedDiscoveryConfigurationRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedDiscoveryConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAutomatedDiscoveryConfigurationRequest:
    out: GetAutomatedDiscoveryConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
