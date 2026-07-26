"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TeletextPageType``."""

from typing import Literal, TypeAlias, cast

"""A page type as defined in the standard ETSI EN 300 468, Table 94"""
TeletextPageType: TypeAlias = Literal[
    "PAGE_TYPE_INITIAL",
    "PAGE_TYPE_SUBTITLE",
    "PAGE_TYPE_ADDL_INFO",
    "PAGE_TYPE_PROGRAM_SCHEDULE",
    "PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TeletextPageType) -> str:
    return value


def deserialize_json(data: str) -> TeletextPageType:
    return cast(TeletextPageType, data)
