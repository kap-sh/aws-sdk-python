"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UpgradeStep``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

UpgradeStep: TypeAlias = Literal[
    "PRE_UPGRADE_CHECK",
    "SNAPSHOT",
    "UPGRADE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRE_UPGRADE_CHECK",
        "SNAPSHOT",
        "UPGRADE",
    )
)


def serialize_json(value: UpgradeStep) -> str:
    return value


def deserialize_json(data: str) -> UpgradeStep:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpgradeStep value: {data!r}")
    return cast(UpgradeStep, data)
