"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsCaptionLanguageSetting``."""

from typing import Literal, TypeAlias, cast

"""Applies only to 608 Embedded output captions. Insert: Include CLOSED-CAPTIONS lines in the manifest. Specify at least one language in the CC1 Language Code field. One CLOSED-CAPTION line is added for each Language Code you specify. Make sure to specify the languages in the order in which they appear in the original source (if the source is embedded format) or the order of the caption selectors (if the source is other than embedded). Otherwise, languages in the manifest will not match up properly with the output captions. None: Include CLOSED-CAPTIONS=NONE line in the manifest. Omit: Omit any CLOSED-CAPTIONS line from the manifest."""
HlsCaptionLanguageSetting: TypeAlias = Literal[
    "INSERT",
    "OMIT",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsCaptionLanguageSetting) -> str:
    return value


def deserialize_json(data: str) -> HlsCaptionLanguageSetting:
    return cast(HlsCaptionLanguageSetting, data)
