"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainAvailability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route_53_domains.errors import DeserializationError

DomainAvailability: TypeAlias = Literal[
    "AVAILABLE",
    "AVAILABLE_RESERVED",
    "AVAILABLE_PREORDER",
    "UNAVAILABLE",
    "UNAVAILABLE_PREMIUM",
    "UNAVAILABLE_RESTRICTED",
    "RESERVED",
    "DONT_KNOW",
    "INVALID_NAME_FOR_TLD",
    "PENDING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "AVAILABLE_RESERVED",
        "AVAILABLE_PREORDER",
        "UNAVAILABLE",
        "UNAVAILABLE_PREMIUM",
        "UNAVAILABLE_RESTRICTED",
        "RESERVED",
        "DONT_KNOW",
        "INVALID_NAME_FOR_TLD",
        "PENDING",
    )
)


def serialize_aws_json_1_1(value: DomainAvailability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainAvailability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainAvailability value: {data!r}")
    return cast(DomainAvailability, data)
