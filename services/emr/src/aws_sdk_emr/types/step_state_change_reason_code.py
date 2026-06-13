"""Generated from Smithy shape ``com.amazonaws.emr#StepStateChangeReasonCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

StepStateChangeReasonCode: TypeAlias = Literal["NONE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("NONE",))


def serialize_aws_json_1_1(value: StepStateChangeReasonCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepStateChangeReasonCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepStateChangeReasonCode value: {data!r}")
    return cast(StepStateChangeReasonCode, data)
