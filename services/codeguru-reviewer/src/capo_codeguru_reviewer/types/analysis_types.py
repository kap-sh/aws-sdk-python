"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#AnalysisTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.analysis_type

AnalysisTypes: TypeAlias = list[
    "capo_codeguru_reviewer.types.analysis_type.AnalysisType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTypes) -> list:
    import capo_codeguru_reviewer.types.analysis_type

    out: list = []
    for item in value:
        out.append(capo_codeguru_reviewer.types.analysis_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisTypes:
    import capo_codeguru_reviewer.types.analysis_type

    out: AnalysisTypes = []
    for item in data:
        out.append(capo_codeguru_reviewer.types.analysis_type.deserialize_json(item))
    return out
