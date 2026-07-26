"""Generated from Smithy shape ``com.amazonaws.taxsettings#IsraelDealerType``."""

from typing import Literal, TypeAlias, cast

IsraelDealerType: TypeAlias = Literal[
    "Authorized",
    "Non-authorized",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsraelDealerType) -> str:
    return value


def deserialize_json(data: str) -> IsraelDealerType:
    return cast(IsraelDealerType, data)
