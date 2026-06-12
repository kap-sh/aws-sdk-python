"""Generated from Smithy shape ``com.amazonaws.sagemaker#RoutingStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

RoutingStrategy: TypeAlias = Literal[
    "LEAST_OUTSTANDING_REQUESTS",
    "RANDOM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEAST_OUTSTANDING_REQUESTS",
        "RANDOM",
    )
)


def serialize_aws_json_1_1(value: RoutingStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RoutingStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutingStrategy value: {data!r}")
    return cast(RoutingStrategy, data)
