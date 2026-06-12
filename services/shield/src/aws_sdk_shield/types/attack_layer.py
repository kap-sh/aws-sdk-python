"""Generated from Smithy shape ``com.amazonaws.shield#AttackLayer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_shield.errors import DeserializationError

AttackLayer: TypeAlias = Literal[
    "NETWORK",
    "APPLICATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NETWORK",
        "APPLICATION",
    )
)


def serialize_aws_json_1_1(value: AttackLayer) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttackLayer:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttackLayer value: {data!r}")
    return cast(AttackLayer, data)
