"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateNetworkProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.long
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.network_profile_type
    import aws_sdk_device_farm.types.percent_integer


class CreateNetworkProfileRequest(TypedDict):
    project_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the project for which you want to create a network profile.</p>"""
    name: "aws_sdk_device_farm.types.name.Name"
    """<p>The name for the new network profile.</p>"""
    description: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>The description of the network profile.</p>"""
    type: NotRequired[
        "aws_sdk_device_farm.types.network_profile_type.NetworkProfileType"
    ]
    """<p>The type of network profile to create. Valid values are listed here.</p>"""
    uplink_bandwidth_bits: NotRequired["aws_sdk_device_farm.types.long.Long"]
    """<p>The data throughput rate in bits per second, as an integer from 0 to 104857600.</p>"""
    downlink_bandwidth_bits: NotRequired["aws_sdk_device_farm.types.long.Long"]
    """<p>The data throughput rate in bits per second, as an integer from 0 to 104857600.</p>"""
    uplink_delay_ms: NotRequired["aws_sdk_device_farm.types.long.Long"]
    """<p>Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.</p>"""
    downlink_delay_ms: NotRequired["aws_sdk_device_farm.types.long.Long"]
    """<p>Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.</p>"""
    uplink_jitter_ms: NotRequired["aws_sdk_device_farm.types.long.Long"]
    """<p>Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.</p>"""
    downlink_jitter_ms: NotRequired["aws_sdk_device_farm.types.long.Long"]
    """<p>Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000.</p>"""
    uplink_loss_percent: "aws_sdk_device_farm.types.percent_integer.PercentInteger"
    """<p>Proportion of transmitted packets that fail to arrive from 0 to 100 percent.</p>"""
    downlink_loss_percent: "aws_sdk_device_farm.types.percent_integer.PercentInteger"
    """<p>Proportion of received packets that fail to arrive from 0 to 100 percent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNetworkProfileRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import aws_sdk_device_farm.types.network_profile_type

        out["type"] = (
            aws_sdk_device_farm.types.network_profile_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "uplink_bandwidth_bits" in value:
        out["uplinkBandwidthBits"] = value["uplink_bandwidth_bits"]
    if "downlink_bandwidth_bits" in value:
        out["downlinkBandwidthBits"] = value["downlink_bandwidth_bits"]
    if "uplink_delay_ms" in value:
        out["uplinkDelayMs"] = value["uplink_delay_ms"]
    if "downlink_delay_ms" in value:
        out["downlinkDelayMs"] = value["downlink_delay_ms"]
    if "uplink_jitter_ms" in value:
        out["uplinkJitterMs"] = value["uplink_jitter_ms"]
    if "downlink_jitter_ms" in value:
        out["downlinkJitterMs"] = value["downlink_jitter_ms"]
    out["uplinkLossPercent"] = value.get("uplink_loss_percent", 0)
    out["downlinkLossPercent"] = value.get("downlink_loss_percent", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNetworkProfileRequest:
    out: CreateNetworkProfileRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("CreateNetworkProfileRequest.project_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateNetworkProfileRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_device_farm.types.network_profile_type

        out["type"] = (
            aws_sdk_device_farm.types.network_profile_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    if "uplinkBandwidthBits" in data:
        out["uplink_bandwidth_bits"] = data["uplinkBandwidthBits"]
    if "downlinkBandwidthBits" in data:
        out["downlink_bandwidth_bits"] = data["downlinkBandwidthBits"]
    if "uplinkDelayMs" in data:
        out["uplink_delay_ms"] = data["uplinkDelayMs"]
    if "downlinkDelayMs" in data:
        out["downlink_delay_ms"] = data["downlinkDelayMs"]
    if "uplinkJitterMs" in data:
        out["uplink_jitter_ms"] = data["uplinkJitterMs"]
    if "downlinkJitterMs" in data:
        out["downlink_jitter_ms"] = data["downlinkJitterMs"]
    if "uplinkLossPercent" in data:
        out["uplink_loss_percent"] = data["uplinkLossPercent"]
    else:
        out["uplink_loss_percent"] = 0
    if "downlinkLossPercent" in data:
        out["downlink_loss_percent"] = data["downlinkLossPercent"]
    else:
        out["downlink_loss_percent"] = 0
    return out
