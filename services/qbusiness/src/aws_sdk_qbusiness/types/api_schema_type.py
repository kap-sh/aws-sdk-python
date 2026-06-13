"""Generated from Smithy shape ``com.amazonaws.qbusiness#APISchemaType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

APISchemaType: TypeAlias = Literal["OPEN_API_V3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OPEN_API_V3",))


def serialize_json(value: APISchemaType) -> str:
    return value


def deserialize_json(data: str) -> APISchemaType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown APISchemaType value: {data!r}")
    return cast(APISchemaType, data)
