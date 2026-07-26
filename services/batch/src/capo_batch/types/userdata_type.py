"""Generated from Smithy shape ``com.amazonaws.batch#UserdataType``."""

from typing import Literal, TypeAlias, cast

UserdataType: TypeAlias = Literal[
    "EKS_BOOTSTRAP_SH",
    "EKS_NODEADM",
]


# --- restJson1 ser/de ---
def serialize_json(value: UserdataType) -> str:
    return value


def deserialize_json(data: str) -> UserdataType:
    return cast(UserdataType, data)
