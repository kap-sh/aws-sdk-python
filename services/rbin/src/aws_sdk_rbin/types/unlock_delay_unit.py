"""Generated from Smithy shape ``com.amazonaws.rbin#UnlockDelayUnit``."""

from typing import Literal, TypeAlias, cast

UnlockDelayUnit: TypeAlias = Literal["DAYS",]


# --- restJson1 ser/de ---
def serialize_json(value: UnlockDelayUnit) -> str:
    return value


def deserialize_json(data: str) -> UnlockDelayUnit:
    return cast(UnlockDelayUnit, data)
