"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentComponentUpdatePolicyAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_greengrassv2.errors import DeserializationError

DeploymentComponentUpdatePolicyAction: TypeAlias = Literal[
    "NOTIFY_COMPONENTS",
    "SKIP_NOTIFY_COMPONENTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOTIFY_COMPONENTS",
        "SKIP_NOTIFY_COMPONENTS",
    )
)


def serialize_json(value: DeploymentComponentUpdatePolicyAction) -> str:
    return value


def deserialize_json(data: str) -> DeploymentComponentUpdatePolicyAction:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeploymentComponentUpdatePolicyAction value: {data!r}"
        )
    return cast(DeploymentComponentUpdatePolicyAction, data)
