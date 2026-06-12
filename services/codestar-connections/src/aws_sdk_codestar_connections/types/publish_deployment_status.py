"""Generated from Smithy shape ``com.amazonaws.codestarconnections#PublishDeploymentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_connections.errors import DeserializationError

PublishDeploymentStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: PublishDeploymentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PublishDeploymentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PublishDeploymentStatus value: {data!r}")
    return cast(PublishDeploymentStatus, data)
