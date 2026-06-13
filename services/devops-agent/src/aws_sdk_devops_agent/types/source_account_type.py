"""Generated from Smithy shape ``com.amazonaws.devopsagent#SourceAccountType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_agent.errors import DeserializationError

"""<p>AWS association type for source account.</p>"""
SourceAccountType: TypeAlias = Literal["source",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("source",))


def serialize_json(value: SourceAccountType) -> str:
    return value


def deserialize_json(data: str) -> SourceAccountType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceAccountType value: {data!r}")
    return cast(SourceAccountType, data)
