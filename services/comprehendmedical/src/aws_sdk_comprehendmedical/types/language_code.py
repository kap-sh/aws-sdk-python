"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#LanguageCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

LanguageCode: TypeAlias = Literal["en",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("en",))


def serialize_aws_json_1_1(value: LanguageCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LanguageCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LanguageCode value: {data!r}")
    return cast(LanguageCode, data)
