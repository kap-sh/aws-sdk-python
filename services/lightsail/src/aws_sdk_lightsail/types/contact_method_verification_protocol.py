"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactMethodVerificationProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

ContactMethodVerificationProtocol: TypeAlias = Literal["Email",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Email",))


def serialize_aws_json_1_1(value: ContactMethodVerificationProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactMethodVerificationProtocol:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContactMethodVerificationProtocol value: {data!r}"
        )
    return cast(ContactMethodVerificationProtocol, data)
