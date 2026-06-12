"""Generated from Smithy shape ``com.amazonaws.guardduty#FeatureAdditionalConfiguration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

FeatureAdditionalConfiguration: TypeAlias = Literal[
    "EKS_ADDON_MANAGEMENT",
    "ECS_FARGATE_AGENT_MANAGEMENT",
    "EC2_AGENT_MANAGEMENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EKS_ADDON_MANAGEMENT",
        "ECS_FARGATE_AGENT_MANAGEMENT",
        "EC2_AGENT_MANAGEMENT",
    )
)


def serialize_json(value: FeatureAdditionalConfiguration) -> str:
    return value


def deserialize_json(data: str) -> FeatureAdditionalConfiguration:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FeatureAdditionalConfiguration value: {data!r}"
        )
    return cast(FeatureAdditionalConfiguration, data)
