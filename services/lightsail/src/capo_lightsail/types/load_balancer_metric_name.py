"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerMetricName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: LoadBalancerMetricName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerMetricName:
    return cast(LoadBalancerMetricName, data)
