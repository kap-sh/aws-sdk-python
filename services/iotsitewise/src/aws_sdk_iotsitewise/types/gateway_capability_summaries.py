"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GatewayCapabilitySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.gateway_capability_summary

GatewayCapabilitySummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.gateway_capability_summary.GatewayCapabilitySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayCapabilitySummaries) -> list:
    import aws_sdk_iotsitewise.types.gateway_capability_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.gateway_capability_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GatewayCapabilitySummaries:
    import aws_sdk_iotsitewise.types.gateway_capability_summary

    out: GatewayCapabilitySummaries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.gateway_capability_summary.deserialize_json(item)
        )
    return out
