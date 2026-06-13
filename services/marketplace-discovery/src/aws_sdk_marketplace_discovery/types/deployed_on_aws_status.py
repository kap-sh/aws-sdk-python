"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DeployedOnAwsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

DeployedOnAwsStatus: TypeAlias = Literal[
    "DEPLOYED",
    "NOT_DEPLOYED",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEPLOYED",
        "NOT_DEPLOYED",
        "NOT_APPLICABLE",
    )
)


def serialize_json(value: DeployedOnAwsStatus) -> str:
    return value


def deserialize_json(data: str) -> DeployedOnAwsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeployedOnAwsStatus value: {data!r}")
    return cast(DeployedOnAwsStatus, data)
