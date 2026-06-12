"""Generated from Smithy shape ``com.amazonaws.pi#AcceptLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

AcceptLanguage: TypeAlias = Literal["EN_US",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EN_US",))


def serialize_aws_json_1_1(value: AcceptLanguage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceptLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AcceptLanguage value: {data!r}")
    return cast(AcceptLanguage, data)
