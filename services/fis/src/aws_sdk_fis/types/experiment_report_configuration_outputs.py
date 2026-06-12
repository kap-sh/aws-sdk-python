"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentReportConfigurationOutputs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_report_configuration_outputs_s3_configuration


class ExperimentReportConfigurationOutputs(TypedDict):
    s3_configuration: NotRequired[
        "aws_sdk_fis.types.experiment_report_configuration_outputs_s3_configuration.ExperimentReportConfigurationOutputsS3Configuration"
    ]
    """<p>The S3 destination for the experiment report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentReportConfigurationOutputs) -> dict:
    out: dict = {}
    if "s3_configuration" in value:
        import aws_sdk_fis.types.experiment_report_configuration_outputs_s3_configuration

        out["s3Configuration"] = (
            aws_sdk_fis.types.experiment_report_configuration_outputs_s3_configuration.serialize_json(
                value["s3_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExperimentReportConfigurationOutputs:
    out: ExperimentReportConfigurationOutputs = {}  # type: ignore[typeddict-item]
    if "s3Configuration" in data:
        import aws_sdk_fis.types.experiment_report_configuration_outputs_s3_configuration

        out["s3_configuration"] = (
            aws_sdk_fis.types.experiment_report_configuration_outputs_s3_configuration.deserialize_json(
                data["s3Configuration"]
            )
        )
    return out
