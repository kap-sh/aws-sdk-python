"""Generated from Smithy shape ``com.amazonaws.kendra#Mode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

Mode: TypeAlias = Literal[
    "ENABLED",
    "LEARN_ONLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "LEARN_ONLY",
    )
)


def serialize_aws_json_1_1(value: Mode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Mode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mode value: {data!r}")
    return cast(Mode, data)
