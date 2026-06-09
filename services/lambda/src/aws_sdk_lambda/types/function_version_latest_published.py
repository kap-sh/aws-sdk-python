"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersionLatestPublished``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

FunctionVersionLatestPublished: TypeAlias = Literal["LATEST_PUBLISHED",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LATEST_PUBLISHED",))


def serialize_json(value: FunctionVersionLatestPublished) -> str:
    return value


def deserialize_json(data: str) -> FunctionVersionLatestPublished:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FunctionVersionLatestPublished value: {data!r}"
        )
    return cast(FunctionVersionLatestPublished, data)
