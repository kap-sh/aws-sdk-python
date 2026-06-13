"""Generated from Smithy shape ``com.amazonaws.pcs#SlurmRestMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

SlurmRestMode: TypeAlias = Literal[
    "STANDARD",
    "NONE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "NONE",
    )
)


def serialize_aws_json_1_0(value: SlurmRestMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SlurmRestMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SlurmRestMode value: {data!r}")
    return cast(SlurmRestMode, data)
