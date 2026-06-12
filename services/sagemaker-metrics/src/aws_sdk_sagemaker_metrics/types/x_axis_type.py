"""Generated from Smithy shape ``com.amazonaws.sagemakermetrics#XAxisType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_metrics.errors import DeserializationError

XAxisType: TypeAlias = Literal[
    "IterationNumber",
    "Timestamp",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IterationNumber",
        "Timestamp",
    )
)


def serialize_json(value: XAxisType) -> str:
    return value


def deserialize_json(data: str) -> XAxisType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown XAxisType value: {data!r}")
    return cast(XAxisType, data)
