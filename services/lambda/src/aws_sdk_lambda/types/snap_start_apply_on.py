"""Generated from Smithy shape ``com.amazonaws.lambda#SnapStartApplyOn``."""

from typing import Literal, TypeAlias, cast

SnapStartApplyOn: TypeAlias = Literal[
    "PublishedVersions",
    "None",
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapStartApplyOn) -> str:
    return value


def deserialize_json(data: str) -> SnapStartApplyOn:
    return cast(SnapStartApplyOn, data)
