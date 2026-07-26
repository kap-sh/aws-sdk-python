"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeGatewayCapabilityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.capability_namespace
    import capo_iotsitewise.types.id


class DescribeGatewayCapabilityConfigurationRequest(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway that defines the capability configuration.</p>"""
    capability_namespace: (
        "capo_iotsitewise.types.capability_namespace.CapabilityNamespace"
    )
    """<p>The namespace of the capability configuration. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:3</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayCapabilityConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGatewayCapabilityConfigurationRequest:
    out: DescribeGatewayCapabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
