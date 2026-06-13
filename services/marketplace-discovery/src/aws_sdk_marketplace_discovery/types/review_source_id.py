"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ReviewSourceId``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

ReviewSourceId: TypeAlias = Literal["AWS_MARKETPLACE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWS_MARKETPLACE",))


def serialize_json(value: ReviewSourceId) -> str:
    return value


def deserialize_json(data: str) -> ReviewSourceId:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReviewSourceId value: {data!r}")
    return cast(ReviewSourceId, data)
