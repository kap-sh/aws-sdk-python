"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#NeptuneUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

NeptuneUngracefulBehavior: TypeAlias = Literal["failover",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("failover",))


def serialize_aws_json_1_0(value: NeptuneUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NeptuneUngracefulBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NeptuneUngracefulBehavior value: {data!r}")
    return cast(NeptuneUngracefulBehavior, data)
