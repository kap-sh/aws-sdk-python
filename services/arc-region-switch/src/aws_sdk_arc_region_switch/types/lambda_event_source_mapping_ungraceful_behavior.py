"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#LambdaEventSourceMappingUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_arc_region_switch.errors import DeserializationError

LambdaEventSourceMappingUngracefulBehavior: TypeAlias = Literal["skip",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("skip",))


def serialize_aws_json_1_0(value: LambdaEventSourceMappingUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaEventSourceMappingUngracefulBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown LambdaEventSourceMappingUngracefulBehavior value: {data!r}"
        )
    return cast(LambdaEventSourceMappingUngracefulBehavior, data)
