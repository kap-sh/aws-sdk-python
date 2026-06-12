"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DateTimeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_dashboards.errors import DeserializationError

DateTimeType: TypeAlias = Literal[
    "ABSOLUTE",
    "RELATIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ABSOLUTE",
        "RELATIVE",
    )
)


def serialize_aws_json_1_0(value: DateTimeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DateTimeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DateTimeType value: {data!r}")
    return cast(DateTimeType, data)
