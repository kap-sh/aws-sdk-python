"""Generated from Smithy shape ``com.amazonaws.snowball#ImpactLevel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

ImpactLevel: TypeAlias = Literal[
    "IL2",
    "IL4",
    "IL5",
    "IL6",
    "IL99",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IL2",
        "IL4",
        "IL5",
        "IL6",
        "IL99",
    )
)


def serialize_aws_json_1_1(value: ImpactLevel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ImpactLevel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ImpactLevel value: {data!r}")
    return cast(ImpactLevel, data)
