"""Generated from Smithy shape ``com.amazonaws.guardduty#PublicBucketRestrictBehavior``."""

from typing import Literal, TypeAlias, cast

PublicBucketRestrictBehavior: TypeAlias = Literal[
    "RESTRICTED",
    "NOT_RESTRICTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PublicBucketRestrictBehavior) -> str:
    return value


def deserialize_json(data: str) -> PublicBucketRestrictBehavior:
    return cast(PublicBucketRestrictBehavior, data)
