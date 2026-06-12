"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.capability_report_endpoint

CapabilityReportEndpoints: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.capability_report_endpoint.CapabilityReportEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportEndpoints) -> list:
    import aws_sdk_iot_managed_integrations.types.capability_report_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.capability_report_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CapabilityReportEndpoints:
    import aws_sdk_iot_managed_integrations.types.capability_report_endpoint

    out: CapabilityReportEndpoints = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.capability_report_endpoint.deserialize_json(
                item
            )
        )
    return out
