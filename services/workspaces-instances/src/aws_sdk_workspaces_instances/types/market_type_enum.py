"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#MarketTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_instances.errors import DeserializationError

MarketTypeEnum: TypeAlias = Literal[
    "spot",
    "capacity-block",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "spot",
        "capacity-block",
    )
)


def serialize_aws_json_1_0(value: MarketTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MarketTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MarketTypeEnum value: {data!r}")
    return cast(MarketTypeEnum, data)
