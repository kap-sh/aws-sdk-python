"""Generated from Smithy shape ``com.amazonaws.macie2#UserIdentityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of entity that performed the action on the affected resource. Possible values are:</p>"""
UserIdentityType: TypeAlias = Literal[
    "AssumedRole",
    "IAMUser",
    "FederatedUser",
    "Root",
    "AWSAccount",
    "AWSService",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentityType) -> str:
    return value


def deserialize_json(data: str) -> UserIdentityType:
    return cast(UserIdentityType, data)
