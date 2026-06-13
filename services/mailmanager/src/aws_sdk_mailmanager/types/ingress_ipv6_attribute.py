"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressIpv6Attribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressIpv6Attribute: TypeAlias = Literal["SENDER_IPV6",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("SENDER_IPV6",))


def serialize_aws_json_1_0(value: IngressIpv6Attribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressIpv6Attribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngressIpv6Attribute value: {data!r}")
    return cast(IngressIpv6Attribute, data)
