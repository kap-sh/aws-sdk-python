"""Generated from Smithy shape ``com.amazonaws.ebs#ChecksumAggregationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

ChecksumAggregationMethod: TypeAlias = Literal["LINEAR",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LINEAR",))


def serialize_json(value: ChecksumAggregationMethod) -> str:
    return value


def deserialize_json(data: str) -> ChecksumAggregationMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChecksumAggregationMethod value: {data!r}")
    return cast(ChecksumAggregationMethod, data)
