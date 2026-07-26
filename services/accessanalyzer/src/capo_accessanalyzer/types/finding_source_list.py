"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingSourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_accessanalyzer.types.finding_source

FindingSourceList: TypeAlias = list[
    "capo_accessanalyzer.types.finding_source.FindingSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingSourceList) -> list:
    import capo_accessanalyzer.types.finding_source

    out: list = []
    for item in value:
        out.append(capo_accessanalyzer.types.finding_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> FindingSourceList:
    import capo_accessanalyzer.types.finding_source

    out: FindingSourceList = []
    for item in data:
        out.append(capo_accessanalyzer.types.finding_source.deserialize_json(item))
    return out
