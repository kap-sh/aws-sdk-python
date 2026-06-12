"""Generated from Smithy shape ``com.amazonaws.b2bi#TransformerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_b2bi.errors import DeserializationError

TransformerStatus: TypeAlias = Literal[
    "active",
    "inactive",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "active",
        "inactive",
    )
)


def serialize_aws_json_1_0(value: TransformerStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TransformerStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransformerStatus value: {data!r}")
    return cast(TransformerStatus, data)
