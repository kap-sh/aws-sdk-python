"""Generated from Smithy shape ``com.amazonaws.guardduty#OrgFeatureAdditionalConfiguration``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

OrgFeatureAdditionalConfiguration: TypeAlias = Literal[
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


def serialize_json(value: OrgFeatureAdditionalConfiguration) -> str:
    return value


def deserialize_json(data: str) -> OrgFeatureAdditionalConfiguration:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OrgFeatureAdditionalConfiguration value: {data!r}"
        )
    return cast(OrgFeatureAdditionalConfiguration, data)
