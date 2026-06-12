"""Generated from Smithy shape ``com.amazonaws.sesv2#ReputationEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The type of reputation entity. Currently, only <code>RESOURCE</code> type entities are supported, which represent resources in your Amazon SES account that have reputation tracking capabilities.</p>"""
ReputationEntityType: TypeAlias = Literal["RESOURCE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("RESOURCE",))


def serialize_json(value: ReputationEntityType) -> str:
    return value


def deserialize_json(data: str) -> ReputationEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReputationEntityType value: {data!r}")
    return cast(ReputationEntityType, data)
