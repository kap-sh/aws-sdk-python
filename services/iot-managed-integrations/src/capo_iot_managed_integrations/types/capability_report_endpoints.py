"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_report_endpoint

CapabilityReportEndpoints: TypeAlias = list[
    "capo_iot_managed_integrations.types.capability_report_endpoint.CapabilityReportEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportEndpoints) -> list:
    import capo_iot_managed_integrations.types.capability_report_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.capability_report_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CapabilityReportEndpoints:
    import capo_iot_managed_integrations.types.capability_report_endpoint

    out: CapabilityReportEndpoints = []
    for item in data:
        out.append(
            capo_iot_managed_integrations.types.capability_report_endpoint.deserialize_json(
                item
            )
        )
    return out
