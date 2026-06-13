"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressAddressListEmailAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

IngressAddressListEmailAttribute: TypeAlias = Literal["RECIPIENT",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("RECIPIENT",))


def serialize_aws_json_1_0(value: IngressAddressListEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressAddressListEmailAttribute:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IngressAddressListEmailAttribute value: {data!r}"
        )
    return cast(IngressAddressListEmailAttribute, data)
