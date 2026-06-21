"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneDesiredState``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the Auto-Tune desired state. Valid values are ENABLED, DISABLED.</p>"""
AutoTuneDesiredState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneDesiredState) -> str:
    return value


def deserialize_json(data: str) -> AutoTuneDesiredState:
    return cast(AutoTuneDesiredState, data)
