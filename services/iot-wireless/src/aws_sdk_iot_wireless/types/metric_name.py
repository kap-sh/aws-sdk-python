"""Generated from Smithy shape ``com.amazonaws.iotwireless#MetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: MetricName) -> str:
    return value


def deserialize_json(data: str) -> MetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricName value: {data!r}")
    return cast(MetricName, data)
