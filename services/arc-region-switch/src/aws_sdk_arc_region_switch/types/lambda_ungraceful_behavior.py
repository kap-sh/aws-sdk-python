"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#LambdaUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

LambdaUngracefulBehavior: TypeAlias = Literal["skip",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("skip",))


def serialize_aws_json_1_0(value: LambdaUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaUngracefulBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LambdaUngracefulBehavior value: {data!r}")
    return cast(LambdaUngracefulBehavior, data)
