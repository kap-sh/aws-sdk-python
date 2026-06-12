"""Generated from Smithy shape ``com.amazonaws.shield#ProtectedResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

ProtectedResourceType: TypeAlias = Literal[
    "CLOUDFRONT_DISTRIBUTION",
    "ROUTE_53_HOSTED_ZONE",
    "ELASTIC_IP_ALLOCATION",
    "CLASSIC_LOAD_BALANCER",
    "APPLICATION_LOAD_BALANCER",
    "GLOBAL_ACCELERATOR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUDFRONT_DISTRIBUTION",
        "ROUTE_53_HOSTED_ZONE",
        "ELASTIC_IP_ALLOCATION",
        "CLASSIC_LOAD_BALANCER",
        "APPLICATION_LOAD_BALANCER",
        "GLOBAL_ACCELERATOR",
    )
)


def serialize_aws_json_1_1(value: ProtectedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProtectedResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtectedResourceType value: {data!r}")
    return cast(ProtectedResourceType, data)
