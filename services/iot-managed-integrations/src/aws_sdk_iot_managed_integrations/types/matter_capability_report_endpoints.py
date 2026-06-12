"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint

MatterCapabilityReportEndpoints: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint.MatterCapabilityReportEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportEndpoints) -> list:
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MatterCapabilityReportEndpoints:
    import aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint

    out: MatterCapabilityReportEndpoints = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.matter_capability_report_endpoint.deserialize_json(
                item
            )
        )
    return out
