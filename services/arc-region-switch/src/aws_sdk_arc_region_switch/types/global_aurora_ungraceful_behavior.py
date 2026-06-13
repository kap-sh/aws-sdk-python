"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GlobalAuroraUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

GlobalAuroraUngracefulBehavior: TypeAlias = Literal["failover",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("failover",))


def serialize_aws_json_1_0(value: GlobalAuroraUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GlobalAuroraUngracefulBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GlobalAuroraUngracefulBehavior value: {data!r}"
        )
    return cast(GlobalAuroraUngracefulBehavior, data)
