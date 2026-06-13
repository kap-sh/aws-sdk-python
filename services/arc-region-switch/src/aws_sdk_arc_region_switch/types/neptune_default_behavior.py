"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#NeptuneDefaultBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

NeptuneDefaultBehavior: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: NeptuneDefaultBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NeptuneDefaultBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NeptuneDefaultBehavior value: {data!r}")
    return cast(NeptuneDefaultBehavior, data)
