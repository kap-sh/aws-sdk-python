"""Generated from Smithy shape ``com.amazonaws.lightsail#PortMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_protocol
    import capo_lightsail.types.string

PortMap: TypeAlias = dict[
    "capo_lightsail.types.string.string",
    "capo_lightsail.types.container_service_protocol.ContainerServiceProtocol",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PortMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_lightsail.types.container_service_protocol

        out[key] = (
            capo_lightsail.types.container_service_protocol.serialize_aws_json_1_1(
                value
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PortMap:
    out: PortMap = {}
    for key, value in data.items():
        import capo_lightsail.types.container_service_protocol

        out[key] = (
            capo_lightsail.types.container_service_protocol.deserialize_aws_json_1_1(
                value
            )
        )
    return out
