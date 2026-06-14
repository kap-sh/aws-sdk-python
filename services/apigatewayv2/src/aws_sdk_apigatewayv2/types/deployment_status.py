"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#DeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>Represents a deployment status.</p>"""
DeploymentStatus: TypeAlias = Literal[
    "PENDING",
    "FAILED",
    "DEPLOYED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "FAILED",
        "DEPLOYED",
    )
)


def serialize_json(value: DeploymentStatus) -> str:
    return value


def deserialize_json(data: str) -> DeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeploymentStatus value: {data!r}")
    return cast(DeploymentStatus, data)
