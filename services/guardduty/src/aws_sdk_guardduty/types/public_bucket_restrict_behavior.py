"""Generated from Smithy shape ``com.amazonaws.guardduty#PublicBucketRestrictBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

PublicBucketRestrictBehavior: TypeAlias = Literal[
    "RESTRICTED",
    "NOT_RESTRICTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESTRICTED",
        "NOT_RESTRICTED",
    )
)


def serialize_json(value: PublicBucketRestrictBehavior) -> str:
    return value


def deserialize_json(data: str) -> PublicBucketRestrictBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PublicBucketRestrictBehavior value: {data!r}"
        )
    return cast(PublicBucketRestrictBehavior, data)
