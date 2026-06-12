"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#PropagateTags``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_events.errors import DeserializationError

PropagateTags: TypeAlias = Literal["TASK_DEFINITION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TASK_DEFINITION",))


def serialize_aws_json_1_1(value: PropagateTags) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropagateTags:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropagateTags value: {data!r}")
    return cast(PropagateTags, data)
