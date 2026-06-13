"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GlobalAuroraDefaultBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

GlobalAuroraDefaultBehavior: TypeAlias = Literal[
    "switchoverOnly",
    "failover",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "switchoverOnly",
        "failover",
    )
)


def serialize_aws_json_1_0(value: GlobalAuroraDefaultBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GlobalAuroraDefaultBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GlobalAuroraDefaultBehavior value: {data!r}"
        )
    return cast(GlobalAuroraDefaultBehavior, data)
