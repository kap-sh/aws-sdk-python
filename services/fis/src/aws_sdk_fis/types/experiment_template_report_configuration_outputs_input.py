"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateReportConfigurationOutputsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.report_configuration_s3_output_input


class ExperimentTemplateReportConfigurationOutputsInput(TypedDict, closed=True):
    s3_configuration: NotRequired[
        "aws_sdk_fis.types.report_configuration_s3_output_input.ReportConfigurationS3OutputInput"
    ]
    """<p>The S3 destination for the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateReportConfigurationOutputsInput) -> dict:
    out: dict = {}
    if "s3_configuration" in value:
        import aws_sdk_fis.types.report_configuration_s3_output_input

        out["s3Configuration"] = (
            aws_sdk_fis.types.report_configuration_s3_output_input.serialize_json(
                value["s3_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentTemplateReportConfigurationOutputsInput:
    out: ExperimentTemplateReportConfigurationOutputsInput = {}  # type: ignore[typeddict-item]
    if "s3Configuration" in data:
        import aws_sdk_fis.types.report_configuration_s3_output_input

        out["s3_configuration"] = (
            aws_sdk_fis.types.report_configuration_s3_output_input.deserialize_json(
                data["s3Configuration"]
            )
        )
    return out
