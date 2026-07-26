"""Generated from Smithy shape ``com.amazonaws.mediatailor#FillPolicy``."""

from typing import Literal, TypeAlias, cast

FillPolicy: TypeAlias = Literal[
    "FULL_AVAIL_ONLY",
    "PARTIAL_AVAIL",
]


# --- restJson1 ser/de ---
def serialize_json(value: FillPolicy) -> str:
    return value


def deserialize_json(data: str) -> FillPolicy:
    return cast(FillPolicy, data)
