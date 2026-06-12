"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallFailOpenStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

FirewallFailOpenStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "USE_LOCAL_RESOURCE_SETTING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "USE_LOCAL_RESOURCE_SETTING",
    )
)


def serialize_aws_json_1_1(value: FirewallFailOpenStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallFailOpenStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirewallFailOpenStatus value: {data!r}")
    return cast(FirewallFailOpenStatus, data)
