"""Generated from Smithy shape ``com.amazonaws.b2bi#TransformerJobStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

TransformerJobStatus: TypeAlias = Literal[
    "running",
    "succeeded",
    "failed",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "running",
        "succeeded",
        "failed",
    )
)


def serialize_aws_json_1_0(value: TransformerJobStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TransformerJobStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransformerJobStatus value: {data!r}")
    return cast(TransformerJobStatus, data)
