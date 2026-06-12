"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.capability_report_capability

CapabilityReportCapabilities: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.capability_report_capability.CapabilityReportCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportCapabilities) -> list:
    import aws_sdk_iot_managed_integrations.types.capability_report_capability

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.capability_report_capability.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CapabilityReportCapabilities:
    import aws_sdk_iot_managed_integrations.types.capability_report_capability

    out: CapabilityReportCapabilities = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.capability_report_capability.deserialize_json(
                item
            )
        )
    return out
