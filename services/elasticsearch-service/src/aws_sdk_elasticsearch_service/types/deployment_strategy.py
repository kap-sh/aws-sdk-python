"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DeploymentStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

"""<p>Specifies the deployment strategy for the domain. Valid values are <code>Default</code> and <code>CapacityOptimized</code>.</p>"""
DeploymentStrategy: TypeAlias = Literal[
    "Default",
    "CapacityOptimized",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Default",
        "CapacityOptimized",
    )
)


def serialize_json(value: DeploymentStrategy) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStrategy value: {data!r}")
    return cast(DeploymentStrategy, data)
