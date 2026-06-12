"""Generated from Smithy shape ``com.amazonaws.workdocs#AdditionalResponseFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

AdditionalResponseFieldType: TypeAlias = Literal["WEBURL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("WEBURL",))


def serialize_json(value: AdditionalResponseFieldType) -> str:
    return value


def deserialize_json(data: str) -> AdditionalResponseFieldType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdditionalResponseFieldType value: {data!r}"
        )
    return cast(AdditionalResponseFieldType, data)
