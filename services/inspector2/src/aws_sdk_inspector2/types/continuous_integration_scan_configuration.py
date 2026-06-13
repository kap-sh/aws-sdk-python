"""Generated from Smithy shape ``com.amazonaws.inspector2#ContinuousIntegrationScanConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.continuous_integration_scan_supported_events


class ContinuousIntegrationScanConfiguration(TypedDict):
    supported_events: "aws_sdk_inspector2.types.continuous_integration_scan_supported_events.ContinuousIntegrationScanSupportedEvents"
    """<p>The repository events that trigger continuous integration scans, such as pull requests or commits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContinuousIntegrationScanConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.continuous_integration_scan_supported_events

    out["supportedEvents"] = (
        aws_sdk_inspector2.types.continuous_integration_scan_supported_events.serialize_json(
            value["supported_events"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContinuousIntegrationScanConfiguration:
    out: ContinuousIntegrationScanConfiguration = {}  # type: ignore[typeddict-item]
    if "supportedEvents" in data:
        import aws_sdk_inspector2.types.continuous_integration_scan_supported_events

        out["supported_events"] = (
            aws_sdk_inspector2.types.continuous_integration_scan_supported_events.deserialize_json(
                data["supportedEvents"]
            )
        )
    else:
        raise DeserializationError(
            "ContinuousIntegrationScanConfiguration.supported_events required"
        )
    return out
