"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckProvider``."""

from typing import Literal, TypeAlias, cast

CheckProvider: TypeAlias = Literal["TRUSTED_ADVISOR",]


# --- restJson1 ser/de ---
def serialize_json(value: CheckProvider) -> str:
    return value


def deserialize_json(data: str) -> CheckProvider:
    return cast(CheckProvider, data)
