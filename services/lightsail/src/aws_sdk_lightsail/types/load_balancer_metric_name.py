"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerMetricName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerMetricName: TypeAlias = Literal[
    "ClientTLSNegotiationErrorCount",
    "HealthyHostCount",
    "UnhealthyHostCount",
    "HTTPCode_LB_4XX_Count",
    "HTTPCode_LB_5XX_Count",
    "HTTPCode_Instance_2XX_Count",
    "HTTPCode_Instance_3XX_Count",
    "HTTPCode_Instance_4XX_Count",
    "HTTPCode_Instance_5XX_Count",
    "InstanceResponseTime",
    "RejectedConnectionCount",
    "RequestCount",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ClientTLSNegotiationErrorCount",
        "HealthyHostCount",
        "UnhealthyHostCount",
        "HTTPCode_LB_4XX_Count",
        "HTTPCode_LB_5XX_Count",
        "HTTPCode_Instance_2XX_Count",
        "HTTPCode_Instance_3XX_Count",
        "HTTPCode_Instance_4XX_Count",
        "HTTPCode_Instance_5XX_Count",
        "InstanceResponseTime",
        "RejectedConnectionCount",
        "RequestCount",
    )
)


def serialize_aws_json_1_1(value: LoadBalancerMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerMetricName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoadBalancerMetricName value: {data!r}")
    return cast(LoadBalancerMetricName, data)
