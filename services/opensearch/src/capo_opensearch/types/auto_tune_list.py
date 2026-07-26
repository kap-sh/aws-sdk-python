"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.auto_tune

AutoTuneList: TypeAlias = list["capo_opensearch.types.auto_tune.AutoTune"]


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneList) -> list:
    import capo_opensearch.types.auto_tune

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.auto_tune.serialize_json(item))
    return out


def deserialize_json(data: list) -> AutoTuneList:
    import capo_opensearch.types.auto_tune

    out: AutoTuneList = []
    for item in data:
        out.append(capo_opensearch.types.auto_tune.deserialize_json(item))
    return out
