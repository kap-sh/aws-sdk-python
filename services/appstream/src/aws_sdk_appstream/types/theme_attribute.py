"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

ThemeAttribute: TypeAlias = Literal["FOOTER_LINKS",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FOOTER_LINKS",))


def serialize_aws_json_1_1(value: ThemeAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThemeAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThemeAttribute value: {data!r}")
    return cast(ThemeAttribute, data)
