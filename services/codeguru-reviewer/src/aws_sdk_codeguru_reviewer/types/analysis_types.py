"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#AnalysisTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.analysis_type

AnalysisTypes: TypeAlias = list[
    "aws_sdk_codeguru_reviewer.types.analysis_type.AnalysisType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTypes) -> list:
    import aws_sdk_codeguru_reviewer.types.analysis_type

    out: list = []
    for item in value:
        out.append(aws_sdk_codeguru_reviewer.types.analysis_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AnalysisTypes:
    import aws_sdk_codeguru_reviewer.types.analysis_type

    out: AnalysisTypes = []
    for item in data:
        out.append(aws_sdk_codeguru_reviewer.types.analysis_type.deserialize_json(item))
    return out
