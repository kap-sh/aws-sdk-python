"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GatewaySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.gateway_capability_summaries
    import aws_sdk_iotsitewise.types.gateway_name
    import aws_sdk_iotsitewise.types.gateway_platform
    import aws_sdk_iotsitewise.types.gateway_version
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.timestamp


class GatewaySummary(TypedDict):
    gateway_id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the gateway device.</p>"""
    gateway_name: "aws_sdk_iotsitewise.types.gateway_name.GatewayName"
    """<p>The name of the gateway.</p>"""
    gateway_platform: NotRequired[
        "aws_sdk_iotsitewise.types.gateway_platform.GatewayPlatform"
    ]
    gateway_version: NotRequired[
        "aws_sdk_iotsitewise.types.gateway_version.GatewayVersion"
    ]
    """<p>The version of the gateway. A value of <code>3</code> indicates an MQTT-enabled, V3 gateway, while <code>2</code> indicates a Classic streams, V2 gateway.</p>"""
    gateway_capability_summaries: NotRequired[
        "aws_sdk_iotsitewise.types.gateway_capability_summaries.GatewayCapabilitySummaries"
    ]
    r"""<p>A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use <a href=\"https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html\">DescribeGatewayCapabilityConfiguration</a>.</p>"""
    creation_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the gateway was created, in Unix epoch time.</p>"""
    last_update_date: "aws_sdk_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the gateway was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewaySummary) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["gatewayName"] = value["gateway_name"]
    if "gateway_platform" in value:
        import aws_sdk_iotsitewise.types.gateway_platform

        out["gatewayPlatform"] = (
            aws_sdk_iotsitewise.types.gateway_platform.serialize_json(
                value["gateway_platform"]
            )
        )
    if "gateway_version" in value:
        out["gatewayVersion"] = value["gateway_version"]
    if "gateway_capability_summaries" in value:
        import aws_sdk_iotsitewise.types.gateway_capability_summaries

        out["gatewayCapabilitySummaries"] = (
            aws_sdk_iotsitewise.types.gateway_capability_summaries.serialize_json(
                value["gateway_capability_summaries"]
            )
        )
    import aws_sdk_iotsitewise.types.timestamp

    out["creationDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import aws_sdk_iotsitewise.types.timestamp

    out["lastUpdateDate"] = aws_sdk_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    return out


def deserialize_json(data: dict) -> GatewaySummary:
    out: GatewaySummary = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("GatewaySummary.gateway_id required")
    if "gatewayName" in data:
        out["gateway_name"] = data["gatewayName"]
    else:
        raise DeserializationError("GatewaySummary.gateway_name required")
    if "gatewayPlatform" in data:
        import aws_sdk_iotsitewise.types.gateway_platform

        out["gateway_platform"] = (
            aws_sdk_iotsitewise.types.gateway_platform.deserialize_json(
                data["gatewayPlatform"]
            )
        )
    if "gatewayVersion" in data:
        out["gateway_version"] = data["gatewayVersion"]
    if "gatewayCapabilitySummaries" in data:
        import aws_sdk_iotsitewise.types.gateway_capability_summaries

        out["gateway_capability_summaries"] = (
            aws_sdk_iotsitewise.types.gateway_capability_summaries.deserialize_json(
                data["gatewayCapabilitySummaries"]
            )
        )
    if "creationDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["creation_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("GatewaySummary.creation_date required")
    if "lastUpdateDate" in data:
        import aws_sdk_iotsitewise.types.timestamp

        out["last_update_date"] = aws_sdk_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("GatewaySummary.last_update_date required")
    return out
