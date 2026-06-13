"""Generated from Smithy shape ``com.amazonaws.devopsagent#EventChannelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>Event Channel type</p>"""
EventChannelType: TypeAlias = Literal["webhook",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("webhook",))


def serialize_json(value: EventChannelType) -> str:
    return value


def deserialize_json(data: str) -> EventChannelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventChannelType value: {data!r}")
    return cast(EventChannelType, data)
