"""Generated from Smithy shape ``com.amazonaws.glue#InboundIntegrationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.inbound_integration

InboundIntegrationsList: TypeAlias = list[
    "capo_glue.types.inbound_integration.InboundIntegration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InboundIntegrationsList) -> list:
    import capo_glue.types.inbound_integration

    out: list = []
    for item in value:
        out.append(capo_glue.types.inbound_integration.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InboundIntegrationsList:
    import capo_glue.types.inbound_integration

    out: InboundIntegrationsList = []
    for item in data:
        out.append(capo_glue.types.inbound_integration.deserialize_aws_json_1_1(item))
    return out
