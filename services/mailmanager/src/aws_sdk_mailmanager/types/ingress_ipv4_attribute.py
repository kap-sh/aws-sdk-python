"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv4Attribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressIpv4Attribute: TypeAlias = Literal["SENDER_IP",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SENDER_IP",))


def serialize_aws_json_1_0(value: IngressIpv4Attribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressIpv4Attribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngressIpv4Attribute value: {data!r}")
    return cast(IngressIpv4Attribute, data)
