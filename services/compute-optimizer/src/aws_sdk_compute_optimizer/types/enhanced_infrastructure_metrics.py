"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EnhancedInfrastructureMetrics``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

EnhancedInfrastructureMetrics: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
    )
)


def serialize_aws_json_1_0(value: EnhancedInfrastructureMetrics) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EnhancedInfrastructureMetrics:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown EnhancedInfrastructureMetrics value: {data!r}"
        )
    return cast(EnhancedInfrastructureMetrics, data)
