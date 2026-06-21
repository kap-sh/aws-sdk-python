"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneType``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies Auto-Tune type. Valid value is SCHEDULED_ACTION. </p>"""
AutoTuneType: TypeAlias = Literal["SCHEDULED_ACTION",]


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneType) -> str:
    return value


def deserialize_json(data: str) -> AutoTuneType:
    return cast(AutoTuneType, data)
