"""Generated from Smithy shape ``com.amazonaws.appconfig#ActionPoint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

ActionPoint: TypeAlias = Literal[
    "PRE_CREATE_HOSTED_CONFIGURATION_VERSION",
    "PRE_START_DEPLOYMENT",
    "AT_DEPLOYMENT_TICK",
    "ON_DEPLOYMENT_START",
    "ON_DEPLOYMENT_STEP",
    "ON_DEPLOYMENT_BAKING",
    "ON_DEPLOYMENT_COMPLETE",
    "ON_DEPLOYMENT_ROLLED_BACK",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE_CREATE_HOSTED_CONFIGURATION_VERSION",
        "PRE_START_DEPLOYMENT",
        "AT_DEPLOYMENT_TICK",
        "ON_DEPLOYMENT_START",
        "ON_DEPLOYMENT_STEP",
        "ON_DEPLOYMENT_BAKING",
        "ON_DEPLOYMENT_COMPLETE",
        "ON_DEPLOYMENT_ROLLED_BACK",
    )
)


def serialize_json(value: ActionPoint) -> str:
    return value


def deserialize_json(data: str) -> ActionPoint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionPoint value: {data!r}")
    return cast(ActionPoint, data)
