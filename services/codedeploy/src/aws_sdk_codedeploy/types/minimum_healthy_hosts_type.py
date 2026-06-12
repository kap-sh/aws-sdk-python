"""Generated from Smithy shape ``com.amazonaws.codedeploy#MinimumHealthyHostsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codedeploy.errors import DeserializationError

MinimumHealthyHostsType: TypeAlias = Literal[
    "HOST_COUNT",
    "FLEET_PERCENT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOST_COUNT",
        "FLEET_PERCENT",
    )
)


def serialize_aws_json_1_1(value: MinimumHealthyHostsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MinimumHealthyHostsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MinimumHealthyHostsType value: {data!r}")
    return cast(MinimumHealthyHostsType, data)
