"""Generated from Smithy shape ``com.amazonaws.personalize#IngestionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_personalize.errors import DeserializationError

IngestionMode: TypeAlias = Literal[
    "BULK",
    "PUT",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BULK",
        "PUT",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: IngestionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IngestionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IngestionMode value: {data!r}")
    return cast(IngestionMode, data)
