"""Generated from Smithy shape ``com.amazonaws.glue#WorkerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

WorkerType: TypeAlias = Literal[
    "Standard",
    "G.1X",
    "G.2X",
    "G.025X",
    "G.4X",
    "G.8X",
    "Z.2X",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "G.1X",
        "G.2X",
        "G.025X",
        "G.4X",
        "G.8X",
        "Z.2X",
    )
)


def serialize_aws_json_1_1(value: WorkerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkerType value: {data!r}")
    return cast(WorkerType, data)
