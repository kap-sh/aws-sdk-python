"""Generated from Smithy shape ``com.amazonaws.fms#FirewallDeploymentModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

FirewallDeploymentModel: TypeAlias = Literal[
    "CENTRALIZED",
    "DISTRIBUTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CENTRALIZED",
        "DISTRIBUTED",
    )
)


def serialize_aws_json_1_1(value: FirewallDeploymentModel) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FirewallDeploymentModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FirewallDeploymentModel value: {data!r}")
    return cast(FirewallDeploymentModel, data)
