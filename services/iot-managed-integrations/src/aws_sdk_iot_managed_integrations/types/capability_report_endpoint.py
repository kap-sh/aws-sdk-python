"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.capability_report_capabilities
    import aws_sdk_iot_managed_integrations.types.device_types
    import aws_sdk_iot_managed_integrations.types.endpoint_id


class CapabilityReportEndpoint(TypedDict, closed=True):
    id: "aws_sdk_iot_managed_integrations.types.endpoint_id.EndpointId"
    """<p>The id of the endpoint used in the capability report.</p>"""
    device_types: "aws_sdk_iot_managed_integrations.types.device_types.DeviceTypes"
    """<p>The type of device.</p>"""
    capabilities: "aws_sdk_iot_managed_integrations.types.capability_report_capabilities.CapabilityReportCapabilities"
    """<p>The capabilities used in the capability report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportEndpoint) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_iot_managed_integrations.types.device_types

    out["deviceTypes"] = (
        aws_sdk_iot_managed_integrations.types.device_types.serialize_json(
            value["device_types"]
        )
    )
    import aws_sdk_iot_managed_integrations.types.capability_report_capabilities

    out["capabilities"] = (
        aws_sdk_iot_managed_integrations.types.capability_report_capabilities.serialize_json(
            value["capabilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> CapabilityReportEndpoint:
    out: CapabilityReportEndpoint = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CapabilityReportEndpoint.id required")
    if "deviceTypes" in data:
        import aws_sdk_iot_managed_integrations.types.device_types

        out["device_types"] = (
            aws_sdk_iot_managed_integrations.types.device_types.deserialize_json(
                data["deviceTypes"]
            )
        )
    else:
        raise DeserializationError("CapabilityReportEndpoint.device_types required")
    if "capabilities" in data:
        import aws_sdk_iot_managed_integrations.types.capability_report_capabilities

        out["capabilities"] = (
            aws_sdk_iot_managed_integrations.types.capability_report_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    else:
        raise DeserializationError("CapabilityReportEndpoint.capabilities required")
    return out
