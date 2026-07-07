"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetManagedThingCapabilitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.capabilities
    import aws_sdk_iot_managed_integrations.types.capability_report
    import aws_sdk_iot_managed_integrations.types.managed_thing_id


class GetManagedThingCapabilitiesResponse(TypedDict, closed=True):
    managed_thing_id: NotRequired[
        "aws_sdk_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of the device.</p>"""
    capabilities: NotRequired[
        "aws_sdk_iot_managed_integrations.types.capabilities.Capabilities"
    ]
    """<p>The capabilities of the device such as light bulb.</p>"""
    capability_report: NotRequired[
        "aws_sdk_iot_managed_integrations.types.capability_report.CapabilityReport"
    ]
    """<p>A report of the capabilities for the managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedThingCapabilitiesResponse) -> dict:
    out: dict = {}
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "capabilities" in value:
        out["Capabilities"] = value["capabilities"]
    if "capability_report" in value:
        import aws_sdk_iot_managed_integrations.types.capability_report

        out["CapabilityReport"] = (
            aws_sdk_iot_managed_integrations.types.capability_report.serialize_json(
                value["capability_report"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetManagedThingCapabilitiesResponse:
    out: GetManagedThingCapabilitiesResponse = {}  # type: ignore[typeddict-item]
    if "ManagedThingId" in data:
        out["managed_thing_id"] = data["ManagedThingId"]
    if "Capabilities" in data:
        out["capabilities"] = data["Capabilities"]
    if "CapabilityReport" in data:
        import aws_sdk_iot_managed_integrations.types.capability_report

        out["capability_report"] = (
            aws_sdk_iot_managed_integrations.types.capability_report.deserialize_json(
                data["CapabilityReport"]
            )
        )
    return out
