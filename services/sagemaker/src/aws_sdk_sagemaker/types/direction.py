"""Generated from Smithy shape ``com.amazonaws.sagemaker#Direction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

Direction: TypeAlias = Literal[
    "Both",
    "Ascendants",
    "Descendants",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Both",
        "Ascendants",
        "Descendants",
    )
)


def serialize_aws_json_1_1(value: Direction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Direction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Direction value: {data!r}")
    return cast(Direction, data)
