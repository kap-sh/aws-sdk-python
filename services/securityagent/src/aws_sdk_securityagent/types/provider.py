"""Generated from Smithy shape ``com.amazonaws.securityagent#Provider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Third-party provider type.</p>"""
Provider: TypeAlias = Literal["GITHUB",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GITHUB",))


def serialize_json(value: Provider) -> str:
    return value


def deserialize_json(data: str) -> Provider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Provider value: {data!r}")
    return cast(Provider, data)
