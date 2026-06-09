"""Generated from Smithy shape ``com.amazonaws.kms#ImportState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

ImportState: TypeAlias = Literal[
    "IMPORTED",
    "PENDING_IMPORT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMPORTED",
        "PENDING_IMPORT",
    )
)


def serialize_aws_json_1_1(value: ImportState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImportState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImportState value: {data!r}")
    return cast(ImportState, data)
