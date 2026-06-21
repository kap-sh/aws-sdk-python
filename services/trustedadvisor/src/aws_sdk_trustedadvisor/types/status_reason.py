"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#StatusReason``."""

from typing import Literal, TypeAlias, cast

StatusReason: TypeAlias = Literal["no_data_ok",]


# --- restJson1 ser/de ---
def serialize_json(value: StatusReason) -> str:
    return value


def deserialize_json(data: str) -> StatusReason:
    return cast(StatusReason, data)
