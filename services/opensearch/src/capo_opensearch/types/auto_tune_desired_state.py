"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneDesiredState``."""

from typing import Literal, TypeAlias, cast

"""<p>The Auto-Tune desired state. Valid values are ENABLED and DISABLED.</p>"""
AutoTuneDesiredState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneDesiredState) -> str:
    return value


def deserialize_json(data: str) -> AutoTuneDesiredState:
    return cast(AutoTuneDesiredState, data)
