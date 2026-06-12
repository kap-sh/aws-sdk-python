"""Generated from Smithy shape ``com.amazonaws.costexplorer#GenerationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

GenerationStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "PROCESSING",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "PROCESSING",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: GenerationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GenerationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GenerationStatus value: {data!r}")
    return cast(GenerationStatus, data)
