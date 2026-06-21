"""Generated from Smithy shape ``com.amazonaws.medialive#DvbDashAccessibility``."""

from typing import Literal, TypeAlias, cast

"""Dvb Dash Accessibility"""
DvbDashAccessibility: TypeAlias = Literal[
    "DVBDASH_1_VISUALLY_IMPAIRED",
    "DVBDASH_2_HARD_OF_HEARING",
    "DVBDASH_3_SUPPLEMENTAL_COMMENTARY",
    "DVBDASH_4_DIRECTORS_COMMENTARY",
    "DVBDASH_5_EDUCATIONAL_NOTES",
    "DVBDASH_6_MAIN_PROGRAM",
    "DVBDASH_7_CLEAN_FEED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DvbDashAccessibility) -> str:
    return value


def deserialize_json(data: str) -> DvbDashAccessibility:
    return cast(DvbDashAccessibility, data)
