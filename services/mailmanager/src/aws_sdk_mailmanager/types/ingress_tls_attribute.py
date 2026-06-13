"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressTlsAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressTlsAttribute: TypeAlias = Literal["TLS_PROTOCOL",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("TLS_PROTOCOL",))


def serialize_aws_json_1_0(value: IngressTlsAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressTlsAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngressTlsAttribute value: {data!r}")
    return cast(IngressTlsAttribute, data)
