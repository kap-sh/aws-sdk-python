"""Generated from Smithy shape ``com.amazonaws.dax#IsModifiable``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dax.errors import DeserializationError

IsModifiable: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "CONDITIONAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
        "CONDITIONAL",
    )
)


def serialize_aws_json_1_1(value: IsModifiable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IsModifiable:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsModifiable value: {data!r}")
    return cast(IsModifiable, data)
