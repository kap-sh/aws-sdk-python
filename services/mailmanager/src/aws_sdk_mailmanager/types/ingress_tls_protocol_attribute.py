"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsProtocolAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressTlsProtocolAttribute: TypeAlias = Literal[
    "TLS1_2",
    "TLS1_3",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TLS1_2",
        "TLS1_3",
    )
)


def serialize_aws_json_1_0(value: IngressTlsProtocolAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressTlsProtocolAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngressTlsProtocolAttribute value: {data!r}"
        )
    return cast(IngressTlsProtocolAttribute, data)
