"""Generated from Smithy shape ``com.amazonaws.directconnect#LoaContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

LoaContentType: TypeAlias = Literal["application/pdf",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("application/pdf",))


def serialize_aws_json_1_1(value: LoaContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LoaContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LoaContentType value: {data!r}")
    return cast(LoaContentType, data)
