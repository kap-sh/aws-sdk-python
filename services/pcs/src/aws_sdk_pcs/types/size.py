"""Generated from Smithy shape ``com.amazonaws.pcs#Size``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

Size: TypeAlias = Literal[
    "SMALL",
    "MEDIUM",
    "LARGE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMALL",
        "MEDIUM",
        "LARGE",
    )
)


def serialize_aws_json_1_0(value: Size) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Size:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Size value: {data!r}")
    return cast(Size, data)
