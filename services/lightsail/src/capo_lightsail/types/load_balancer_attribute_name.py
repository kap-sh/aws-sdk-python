"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerAttributeName``."""

from typing import Literal, TypeAlias, cast

LoadBalancerAttributeName: TypeAlias = Literal[
    "HealthCheckPath",
    "SessionStickinessEnabled",
    "SessionStickiness_LB_CookieDurationSeconds",
    "HttpsRedirectionEnabled",
    "TlsPolicyName",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerAttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerAttributeName:
    return cast(LoadBalancerAttributeName, data)
