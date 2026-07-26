"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#DeployedOnAwsStatus``."""

from typing import Literal, TypeAlias, cast

DeployedOnAwsStatus: TypeAlias = Literal[
    "DEPLOYED",
    "NOT_DEPLOYED",
    "NOT_APPLICABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeployedOnAwsStatus) -> str:
    return value


def deserialize_json(data: str) -> DeployedOnAwsStatus:
    return cast(DeployedOnAwsStatus, data)
