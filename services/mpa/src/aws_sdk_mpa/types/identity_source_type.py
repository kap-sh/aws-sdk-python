"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceType``."""

from typing import Literal, TypeAlias, cast

IdentitySourceType: TypeAlias = Literal["IAM_IDENTITY_CENTER",]


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceType) -> str:
    return value


def deserialize_json(data: str) -> IdentitySourceType:
    return cast(IdentitySourceType, data)
