"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#VisualType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_dashboards.errors import DeserializationError

VisualType: TypeAlias = Literal[
    "LINE",
    "BAR",
    "STACK",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LINE",
        "BAR",
        "STACK",
    )
)


def serialize_aws_json_1_0(value: VisualType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> VisualType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VisualType value: {data!r}")
    return cast(VisualType, data)
