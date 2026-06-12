"""Generated from Smithy shape ``com.amazonaws.licensemanager#TokenType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

TokenType: TypeAlias = Literal["REFRESH_TOKEN",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("REFRESH_TOKEN",))


def serialize_aws_json_1_1(value: TokenType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TokenType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TokenType value: {data!r}")
    return cast(TokenType, data)
