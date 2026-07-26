"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_job_summary

CodegenJobSummaryList: TypeAlias = list[
    "capo_amplifyuibuilder.types.codegen_job_summary.CodegenJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobSummaryList) -> list:
    import capo_amplifyuibuilder.types.codegen_job_summary

    out: list = []
    for item in value:
        out.append(capo_amplifyuibuilder.types.codegen_job_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodegenJobSummaryList:
    import capo_amplifyuibuilder.types.codegen_job_summary

    out: CodegenJobSummaryList = []
    for item in data:
        out.append(
            capo_amplifyuibuilder.types.codegen_job_summary.deserialize_json(item)
        )
    return out
