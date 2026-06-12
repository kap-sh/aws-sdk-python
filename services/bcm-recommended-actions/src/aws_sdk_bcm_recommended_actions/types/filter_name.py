"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#FilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_recommended_actions.errors import DeserializationError

FilterName: TypeAlias = Literal[
    "FEATURE",
    "SEVERITY",
    "TYPE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FEATURE",
        "SEVERITY",
        "TYPE",
    )
)


def serialize_aws_json_1_0(value: FilterName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FilterName value: {data!r}")
    return cast(FilterName, data)
