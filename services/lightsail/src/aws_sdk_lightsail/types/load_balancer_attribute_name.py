"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerAttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

LoadBalancerAttributeName: TypeAlias = Literal[
    "HealthCheckPath",
    "SessionStickinessEnabled",
    "SessionStickiness_LB_CookieDurationSeconds",
    "HttpsRedirectionEnabled",
    "TlsPolicyName",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HealthCheckPath",
        "SessionStickinessEnabled",
        "SessionStickiness_LB_CookieDurationSeconds",
        "HttpsRedirectionEnabled",
        "TlsPolicyName",
    )
)


def serialize_aws_json_1_1(value: LoadBalancerAttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoadBalancerAttributeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoadBalancerAttributeName value: {data!r}")
    return cast(LoadBalancerAttributeName, data)
