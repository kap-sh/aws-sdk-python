"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ResolutionOption``."""

from typing import Literal, TypeAlias, cast

ResolutionOption: TypeAlias = Literal[
    "HD",
    "FHD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolutionOption) -> str:
    return value


def deserialize_json(data: str) -> ResolutionOption:
    return cast(ResolutionOption, data)
