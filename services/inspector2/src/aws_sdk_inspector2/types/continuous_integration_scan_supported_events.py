"""Generated from Smithy shape ``com.amazonaws.inspector2#ContinuousIntegrationScanSupportedEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.continuous_integration_scan_event

ContinuousIntegrationScanSupportedEvents: TypeAlias = list[
    "aws_sdk_inspector2.types.continuous_integration_scan_event.ContinuousIntegrationScanEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContinuousIntegrationScanSupportedEvents) -> list:
    import aws_sdk_inspector2.types.continuous_integration_scan_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.continuous_integration_scan_event.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ContinuousIntegrationScanSupportedEvents:
    import aws_sdk_inspector2.types.continuous_integration_scan_event

    out: ContinuousIntegrationScanSupportedEvents = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.continuous_integration_scan_event.deserialize_json(
                item
            )
        )
    return out
