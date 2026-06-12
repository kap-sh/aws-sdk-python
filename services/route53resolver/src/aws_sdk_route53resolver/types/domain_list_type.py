"""Generated from Smithy shape ``com.amazonaws.route53resolver#DomainListType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53resolver.errors import DeserializationError

DomainListType: TypeAlias = Literal[
    "THREAT",
    "CONTENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "THREAT",
        "CONTENT",
    )
)


def serialize_aws_json_1_1(value: DomainListType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DomainListType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainListType value: {data!r}")
    return cast(DomainListType, data)
