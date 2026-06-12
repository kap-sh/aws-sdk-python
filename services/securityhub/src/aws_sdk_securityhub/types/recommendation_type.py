"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

RecommendationType: TypeAlias = Literal["UNUSED_PERMISSION_RECOMMENDATION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("UNUSED_PERMISSION_RECOMMENDATION",))


def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationType value: {data!r}")
    return cast(RecommendationType, data)
