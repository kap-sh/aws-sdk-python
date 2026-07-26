"""Generated from Smithy shape ``com.amazonaws.tnb#UpdateSolNetworkType``."""

from typing import Literal, TypeAlias, cast

UpdateSolNetworkType: TypeAlias = Literal[
    "MODIFY_VNF_INFORMATION",
    "UPDATE_NS",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSolNetworkType) -> str:
    return value


def deserialize_json(data: str) -> UpdateSolNetworkType:
    return cast(UpdateSolNetworkType, data)
