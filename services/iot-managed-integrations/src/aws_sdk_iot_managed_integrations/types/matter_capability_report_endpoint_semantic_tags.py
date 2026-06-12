"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportEndpointSemanticTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.endpoint_semantic_tag

MatterCapabilityReportEndpointSemanticTags: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.endpoint_semantic_tag.EndpointSemanticTag"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportEndpointSemanticTags) -> list:
    return list(value)


def deserialize_json(data: list) -> MatterCapabilityReportEndpointSemanticTags:
    return list(data)
