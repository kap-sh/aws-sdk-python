"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StateEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.state_endpoint

StateEndpoints: TypeAlias = list[
    "aws_sdk_iot_managed_integrations.types.state_endpoint.StateEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: StateEndpoints) -> list:
    import aws_sdk_iot_managed_integrations.types.state_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_managed_integrations.types.state_endpoint.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StateEndpoints:
    import aws_sdk_iot_managed_integrations.types.state_endpoint

    out: StateEndpoints = []
    for item in data:
        out.append(
            aws_sdk_iot_managed_integrations.types.state_endpoint.deserialize_json(item)
        )
    return out
