"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.codegen_job_summary

CodegenJobSummaryList: TypeAlias = list[
    "aws_sdk_amplifyuibuilder.types.codegen_job_summary.CodegenJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobSummaryList) -> list:
    import aws_sdk_amplifyuibuilder.types.codegen_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifyuibuilder.types.codegen_job_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CodegenJobSummaryList:
    import aws_sdk_amplifyuibuilder.types.codegen_job_summary

    out: CodegenJobSummaryList = []
    for item in data:
        out.append(
            aws_sdk_amplifyuibuilder.types.codegen_job_summary.deserialize_json(item)
        )
    return out
