"""Generated from Smithy shape ``com.amazonaws.appstream#LastReportGenerationExecutionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.last_report_generation_execution_error

LastReportGenerationExecutionErrors: TypeAlias = list[
    "capo_appstream.types.last_report_generation_execution_error.LastReportGenerationExecutionError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastReportGenerationExecutionErrors) -> list:
    import capo_appstream.types.last_report_generation_execution_error

    out: list = []
    for item in value:
        out.append(
            capo_appstream.types.last_report_generation_execution_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LastReportGenerationExecutionErrors:
    import capo_appstream.types.last_report_generation_execution_error

    out: LastReportGenerationExecutionErrors = []
    for item in data:
        out.append(
            capo_appstream.types.last_report_generation_execution_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
