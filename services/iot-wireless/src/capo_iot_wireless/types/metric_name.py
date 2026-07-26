"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricName``."""

from typing import Literal, TypeAlias, cast

MetricName: TypeAlias = Literal[
    "DeviceRSSI",
    "DeviceSNR",
    "DeviceRoamingRSSI",
    "DeviceRoamingSNR",
    "DeviceUplinkCount",
    "DeviceDownlinkCount",
    "DeviceUplinkLostCount",
    "DeviceUplinkLostRate",
    "DeviceJoinRequestCount",
    "DeviceJoinAcceptCount",
    "DeviceRoamingUplinkCount",
    "DeviceRoamingDownlinkCount",
    "GatewayUpTime",
    "GatewayDownTime",
    "GatewayRSSI",
    "GatewaySNR",
    "GatewayUplinkCount",
    "GatewayDownlinkCount",
    "GatewayJoinRequestCount",
    "GatewayJoinAcceptCount",
    "AwsAccountUplinkCount",
    "AwsAccountDownlinkCount",
    "AwsAccountUplinkLostCount",
    "AwsAccountUplinkLostRate",
    "AwsAccountJoinRequestCount",
    "AwsAccountJoinAcceptCount",
    "AwsAccountRoamingUplinkCount",
    "AwsAccountRoamingDownlinkCount",
    "AwsAccountDeviceCount",
    "AwsAccountGatewayCount",
    "AwsAccountActiveDeviceCount",
    "AwsAccountActiveGatewayCount",
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricName) -> str:
    return value


def deserialize_json(data: str) -> MetricName:
    return cast(MetricName, data)
