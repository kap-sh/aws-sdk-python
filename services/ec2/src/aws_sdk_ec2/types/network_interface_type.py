"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ec2.errors import DeserializationError
from aws_sdk_ec2._protocol.xml import Element

NetworkInterfaceType: TypeAlias = Literal[
    "interface",
    "natGateway",
    "efa",
    "efa-only",
    "trunk",
    "load_balancer",
    "network_load_balancer",
    "vpc_endpoint",
    "branch",
    "transit_gateway",
    "lambda",
    "quicksight",
    "global_accelerator_managed",
    "api_gateway_managed",
    "gateway_load_balancer",
    "gateway_load_balancer_endpoint",
    "iot_rules_managed",
    "aws_codestar_connections_managed",
]


# --- ec2Query ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "interface",
        "natGateway",
        "efa",
        "efa-only",
        "trunk",
        "load_balancer",
        "network_load_balancer",
        "vpc_endpoint",
        "branch",
        "transit_gateway",
        "lambda",
        "quicksight",
        "global_accelerator_managed",
        "api_gateway_managed",
        "gateway_load_balancer",
        "gateway_load_balancer_endpoint",
        "iot_rules_managed",
        "aws_codestar_connections_managed",
    )
)


_VALUES: frozenset[str] = frozenset(
    (
        "interface",
        "natGateway",
        "efa",
        "efa-only",
        "trunk",
        "load_balancer",
        "network_load_balancer",
        "vpc_endpoint",
        "branch",
        "transit_gateway",
        "lambda",
        "quicksight",
        "global_accelerator_managed",
        "api_gateway_managed",
        "gateway_load_balancer",
        "gateway_load_balancer_endpoint",
        "iot_rules_managed",
        "aws_codestar_connections_managed",
    )
)


def to_ec2_query_text(value: NetworkInterfaceType) -> str:
    return value


def from_ec2_query_text(text: str) -> NetworkInterfaceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown NetworkInterfaceType value: {text!r}")
    return cast(NetworkInterfaceType, text)


def serialize_ec2_query(
    value: NetworkInterfaceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_ec2_query_text(value)))


def deserialize_ec2_query(el: Element) -> NetworkInterfaceType:
    return from_ec2_query_text(el.text or "")
