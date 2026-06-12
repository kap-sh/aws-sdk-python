"""Generated from Smithy shape ``com.amazonaws.swf#ChildPolicy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

ChildPolicy: TypeAlias = Literal[
    "TERMINATE",
    "REQUEST_CANCEL",
    "ABANDON",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TERMINATE",
        "REQUEST_CANCEL",
        "ABANDON",
    )
)


def serialize_aws_json_1_0(value: ChildPolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ChildPolicy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChildPolicy value: {data!r}")
    return cast(ChildPolicy, data)
