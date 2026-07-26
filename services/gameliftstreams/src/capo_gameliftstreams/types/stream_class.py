"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamClass``."""

from typing import Literal, TypeAlias, cast

StreamClass: TypeAlias = Literal[
    "gen4n_high",
    "gen4n_ultra",
    "gen4n_win2022",
    "gen5n_high",
    "gen5n_ultra",
    "gen5n_win2022",
    "gen6n_small",
    "gen6n_medium",
    "gen6n_high",
    "gen6n_ultra",
    "gen6n_ultra_win2022",
    "gen6n_pro",
    "gen6n_pro_win2022",
    "gen6n_small_win2022",
    "gen6n_medium_win2022",
    "gen6e_pro",
    "gen6e_pro_win2022",
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamClass) -> str:
    return value


def deserialize_json(data: str) -> StreamClass:
    return cast(StreamClass, data)
