"""Generated from Smithy shape ``com.amazonaws.gamelift#BackfillMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

BackfillMode: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTOMATIC",
        "MANUAL",
    )
)


def serialize_aws_json_1_1(value: BackfillMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BackfillMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackfillMode value: {data!r}")
    return cast(BackfillMode, data)
