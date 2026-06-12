"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

NamespaceType: TypeAlias = Literal[
    "DNS_PUBLIC",
    "DNS_PRIVATE",
    "HTTP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DNS_PUBLIC",
        "DNS_PRIVATE",
        "HTTP",
    )
)


def serialize_aws_json_1_1(value: NamespaceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NamespaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamespaceType value: {data!r}")
    return cast(NamespaceType, data)
