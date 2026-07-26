"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DefaultForUnmappedSignalsType``."""

from typing import Literal, TypeAlias, cast

DefaultForUnmappedSignalsType: TypeAlias = Literal["CUSTOM_DECODING",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DefaultForUnmappedSignalsType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DefaultForUnmappedSignalsType:
    return cast(DefaultForUnmappedSignalsType, data)
