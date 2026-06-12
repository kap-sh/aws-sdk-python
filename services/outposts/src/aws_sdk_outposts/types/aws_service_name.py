"""Generated from Smithy shape ``com.amazonaws.outposts#AWSServiceName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

AWSServiceName: TypeAlias = Literal[
    "AWS",
    "EC2",
    "ELASTICACHE",
    "ELB",
    "RDS",
    "ROUTE53",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS",
        "EC2",
        "ELASTICACHE",
        "ELB",
        "RDS",
        "ROUTE53",
    )
)


def serialize_json(value: AWSServiceName) -> str:
    return value


def deserialize_json(data: str) -> AWSServiceName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AWSServiceName value: {data!r}")
    return cast(AWSServiceName, data)
