"""Generated from Smithy shape ``com.amazonaws.glue#JobMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

JobMode: TypeAlias = Literal[
    "SCRIPT",
    "VISUAL",
    "NOTEBOOK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SCRIPT",
        "VISUAL",
        "NOTEBOOK",
    )
)


def serialize_aws_json_1_1(value: JobMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobMode value: {data!r}")
    return cast(JobMode, data)
