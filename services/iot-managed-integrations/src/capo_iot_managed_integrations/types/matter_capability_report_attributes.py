"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.matter_capability_report_attribute

MatterCapabilityReportAttributes: TypeAlias = list[
    "capo_iot_managed_integrations.types.matter_capability_report_attribute.MatterCapabilityReportAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportAttributes) -> list:
    import capo_iot_managed_integrations.types.matter_capability_report_attribute

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.matter_capability_report_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MatterCapabilityReportAttributes:
    import capo_iot_managed_integrations.types.matter_capability_report_attribute

    out: MatterCapabilityReportAttributes = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.matter_capability_report_attribute.deserialize_json(
                item
            )
        )
    return out
