"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressIpOperator: TypeAlias = Literal[
    "CIDR_MATCHES",
    "NOT_CIDR_MATCHES",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CIDR_MATCHES",
        "NOT_CIDR_MATCHES",
    )
)


def serialize_aws_json_1_0(value: IngressIpOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressIpOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngressIpOperator value: {data!r}")
    return cast(IngressIpOperator, data)
