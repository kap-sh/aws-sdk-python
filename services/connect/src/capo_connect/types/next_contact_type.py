"""Generated from Smithy shape ``com.amazonaws.connect#NextContactType``."""

from typing import Literal, TypeAlias, cast

NextContactType: TypeAlias = Literal["QUICK_CONNECT",]


# --- restJson1 ser/de ---
def serialize_json(value: NextContactType) -> str:
    return value


def deserialize_json(data: str) -> NextContactType:
    return cast(NextContactType, data)
