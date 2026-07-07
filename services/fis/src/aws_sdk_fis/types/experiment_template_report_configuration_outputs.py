"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateReportConfigurationOutputs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.report_configuration_s3_output


class ExperimentTemplateReportConfigurationOutputs(TypedDict, closed=True):
    s3_configuration: NotRequired[
        "aws_sdk_fis.types.report_configuration_s3_output.ReportConfigurationS3Output"
    ]
    """<p>The S3 destination for the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateReportConfigurationOutputs) -> dict:
    out: dict = {}
    if "s3_configuration" in value:
        import aws_sdk_fis.types.report_configuration_s3_output

        out["s3Configuration"] = (
            aws_sdk_fis.types.report_configuration_s3_output.serialize_json(
                value["s3_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentTemplateReportConfigurationOutputs:
    out: ExperimentTemplateReportConfigurationOutputs = {}  # type: ignore[typeddict-item]
    if "s3Configuration" in data:
        import aws_sdk_fis.types.report_configuration_s3_output

        out["s3_configuration"] = (
            aws_sdk_fis.types.report_configuration_s3_output.deserialize_json(
                data["s3Configuration"]
            )
        )
    return out
