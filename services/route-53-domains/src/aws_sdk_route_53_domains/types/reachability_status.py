"""Generated from Smithy shape ``com.amazonaws.route53domains#ReachabilityStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

ReachabilityStatus: TypeAlias = Literal[
    "PENDING",
    "DONE",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "DONE",
        "EXPIRED",
    )
)


def serialize_aws_json_1_1(value: ReachabilityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReachabilityStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReachabilityStatus value: {data!r}")
    return cast(ReachabilityStatus, data)
