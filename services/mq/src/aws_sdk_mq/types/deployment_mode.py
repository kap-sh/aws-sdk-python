"""Generated from Smithy shape ``com.amazonaws.mq#DeploymentMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mq.errors import DeserializationError

"""<p>The broker's deployment mode.</p>"""
DeploymentMode: TypeAlias = Literal[
    "SINGLE_INSTANCE",
    "ACTIVE_STANDBY_MULTI_AZ",
    "CLUSTER_MULTI_AZ",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_INSTANCE",
        "ACTIVE_STANDBY_MULTI_AZ",
        "CLUSTER_MULTI_AZ",
    )
)


def serialize_json(value: DeploymentMode) -> str:
    return value


def deserialize_json(data: str) -> DeploymentMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentMode value: {data!r}")
    return cast(DeploymentMode, data)
