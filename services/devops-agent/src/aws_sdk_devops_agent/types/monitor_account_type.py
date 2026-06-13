"""Generated from Smithy shape ``com.amazonaws.devopsagent#MonitorAccountType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>AWS association type for monitoring account.</p>"""
MonitorAccountType: TypeAlias = Literal["monitor",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("monitor",))


def serialize_json(value: MonitorAccountType) -> str:
    return value


def deserialize_json(data: str) -> MonitorAccountType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MonitorAccountType value: {data!r}")
    return cast(MonitorAccountType, data)
