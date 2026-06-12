"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DefaultForUnmappedSignalsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

DefaultForUnmappedSignalsType: TypeAlias = Literal["CUSTOM_DECODING",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CUSTOM_DECODING",))


def serialize_aws_json_1_0(value: DefaultForUnmappedSignalsType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DefaultForUnmappedSignalsType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DefaultForUnmappedSignalsType value: {data!r}"
        )
    return cast(DefaultForUnmappedSignalsType, data)
