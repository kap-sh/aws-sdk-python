"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsProtocolOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressTlsProtocolOperator: TypeAlias = Literal[
    "MINIMUM_TLS_VERSION",
    "IS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MINIMUM_TLS_VERSION",
        "IS",
    )
)


def serialize_aws_json_1_0(value: IngressTlsProtocolOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressTlsProtocolOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngressTlsProtocolOperator value: {data!r}"
        )
    return cast(IngressTlsProtocolOperator, data)
