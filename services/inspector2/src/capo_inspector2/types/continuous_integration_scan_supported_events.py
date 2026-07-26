"""Generated from Smithy shape ``com.amazonaws.inspector2#ContinuousIntegrationScanSupportedEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.continuous_integration_scan_event

ContinuousIntegrationScanSupportedEvents: TypeAlias = list[
    "capo_inspector2.types.continuous_integration_scan_event.ContinuousIntegrationScanEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContinuousIntegrationScanSupportedEvents) -> list:
    import capo_inspector2.types.continuous_integration_scan_event

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.continuous_integration_scan_event.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContinuousIntegrationScanSupportedEvents:
    import capo_inspector2.types.continuous_integration_scan_event

    out: ContinuousIntegrationScanSupportedEvents = []
    for item in data:
        out.append(
            capo_inspector2.types.continuous_integration_scan_event.deserialize_json(
                item
            )
        )
    return out
