"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResiliencyPolicyTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

ResiliencyPolicyTier: TypeAlias = Literal[
    "MissionCritical",
    "Critical",
    "Important",
    "CoreServices",
    "NonCritical",
    "NotApplicable",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MissionCritical",
        "Critical",
        "Important",
        "CoreServices",
        "NonCritical",
        "NotApplicable",
    )
)


def serialize_json(value: ResiliencyPolicyTier) -> str:
    return value


def deserialize_json(data: str) -> ResiliencyPolicyTier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResiliencyPolicyTier value: {data!r}")
    return cast(ResiliencyPolicyTier, data)
