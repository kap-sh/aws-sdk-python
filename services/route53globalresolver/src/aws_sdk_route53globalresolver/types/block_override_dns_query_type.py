"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BlockOverrideDnsQueryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

BlockOverrideDnsQueryType: TypeAlias = Literal["CNAME",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CNAME",))


def serialize_json(value: BlockOverrideDnsQueryType) -> str:
    return value


def deserialize_json(data: str) -> BlockOverrideDnsQueryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockOverrideDnsQueryType value: {data!r}")
    return cast(BlockOverrideDnsQueryType, data)
