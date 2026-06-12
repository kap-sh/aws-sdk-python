"""Generated from Smithy shape ``com.amazonaws.codeconnections#TriggerResourceUpdateOn``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeconnections.errors import DeserializationError

TriggerResourceUpdateOn: TypeAlias = Literal[
    "ANY_CHANGE",
    "FILE_CHANGE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ANY_CHANGE",
        "FILE_CHANGE",
    )
)


def serialize_aws_json_1_0(value: TriggerResourceUpdateOn) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TriggerResourceUpdateOn:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggerResourceUpdateOn value: {data!r}")
    return cast(TriggerResourceUpdateOn, data)
