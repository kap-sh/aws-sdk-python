"""Generated from Smithy shape ``com.amazonaws.lambda#SnapStartApplyOn``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

SnapStartApplyOn: TypeAlias = Literal[
    "PublishedVersions",
    "None",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PublishedVersions",
        "None",
    )
)


def serialize_json(value: SnapStartApplyOn) -> str:
    return value


def deserialize_json(data: str) -> SnapStartApplyOn:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnapStartApplyOn value: {data!r}")
    return cast(SnapStartApplyOn, data)
