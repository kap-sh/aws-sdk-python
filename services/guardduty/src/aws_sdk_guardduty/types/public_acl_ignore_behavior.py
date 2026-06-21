"""Generated from Smithy shape ``com.amazonaws.guardduty#PublicAclIgnoreBehavior``."""

from typing import Literal, TypeAlias, cast

PublicAclIgnoreBehavior: TypeAlias = Literal[
    "IGNORED",
    "NOT_IGNORED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PublicAclIgnoreBehavior) -> str:
    return value


def deserialize_json(data: str) -> PublicAclIgnoreBehavior:
    return cast(PublicAclIgnoreBehavior, data)
