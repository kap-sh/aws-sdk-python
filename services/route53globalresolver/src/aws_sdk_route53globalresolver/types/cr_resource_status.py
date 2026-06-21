"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#CRResourceStatus``."""

from typing import Literal, TypeAlias, cast

CRResourceStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "UPDATING",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: CRResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> CRResourceStatus:
    return cast(CRResourceStatus, data)
