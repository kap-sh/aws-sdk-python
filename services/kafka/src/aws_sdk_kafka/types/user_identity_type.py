"""Generated from Smithy shape ``com.amazonaws.kafka#UserIdentityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The identity type of the requester that calls the API operation.</p>"""
UserIdentityType: TypeAlias = Literal[
    "AWSACCOUNT",
    "AWSSERVICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentityType) -> str:
    return value


def deserialize_json(data: str) -> UserIdentityType:
    return cast(UserIdentityType, data)
