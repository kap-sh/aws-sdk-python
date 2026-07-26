"""Generated from Smithy shape ``com.amazonaws.macie2#AutoEnableMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies whether to automatically enable automated sensitive data discovery for accounts that are part of an organization in Amazon Macie. Valid values are:</p>"""
AutoEnableMode: TypeAlias = Literal[
    "ALL",
    "NEW",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoEnableMode) -> str:
    return value


def deserialize_json(data: str) -> AutoEnableMode:
    return cast(AutoEnableMode, data)
