"""Generated from Smithy shape ``com.amazonaws.securityagent#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Type of resource.</p>"""
ResourceType: TypeAlias = Literal["CODE_REPOSITORY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CODE_REPOSITORY",))


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
