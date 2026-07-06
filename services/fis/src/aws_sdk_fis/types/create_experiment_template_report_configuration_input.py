"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateReportConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_report_configuration_data_sources_input
    import aws_sdk_fis.types.experiment_template_report_configuration_outputs_input
    import aws_sdk_fis.types.report_configuration_duration


class CreateExperimentTemplateReportConfigurationInput(TypedDict, closed=True):
    outputs: NotRequired[
        "aws_sdk_fis.types.experiment_template_report_configuration_outputs_input.ExperimentTemplateReportConfigurationOutputsInput"
    ]
    """<p>The output destinations of the experiment report. </p>"""
    data_sources: NotRequired[
        "aws_sdk_fis.types.experiment_template_report_configuration_data_sources_input.ExperimentTemplateReportConfigurationDataSourcesInput"
    ]
    """<p>The data sources for the experiment report.</p>"""
    pre_experiment_duration: NotRequired[
        "aws_sdk_fis.types.report_configuration_duration.ReportConfigurationDuration"
    ]
    """<p>The duration before the experiment start time for the data sources to include in the report. </p>"""
    post_experiment_duration: NotRequired[
        "aws_sdk_fis.types.report_configuration_duration.ReportConfigurationDuration"
    ]
    """<p>The duration after the experiment end time for the data sources to include in the report. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateExperimentTemplateReportConfigurationInput) -> dict:
    out: dict = {}
    if "outputs" in value:
        import aws_sdk_fis.types.experiment_template_report_configuration_outputs_input

        out["outputs"] = (
            aws_sdk_fis.types.experiment_template_report_configuration_outputs_input.serialize_json(
                value["outputs"]
            )
        )
    if "data_sources" in value:
        import aws_sdk_fis.types.experiment_template_report_configuration_data_sources_input

        out["dataSources"] = (
            aws_sdk_fis.types.experiment_template_report_configuration_data_sources_input.serialize_json(
                value["data_sources"]
            )
        )
    if "pre_experiment_duration" in value:
        out["preExperimentDuration"] = value["pre_experiment_duration"]
    if "post_experiment_duration" in value:
        out["postExperimentDuration"] = value["post_experiment_duration"]
    return out


def deserialize_json(data: dict) -> CreateExperimentTemplateReportConfigurationInput:
    out: CreateExperimentTemplateReportConfigurationInput = {}  # type: ignore[typeddict-item]
    if "outputs" in data:
        import aws_sdk_fis.types.experiment_template_report_configuration_outputs_input

        out["outputs"] = (
            aws_sdk_fis.types.experiment_template_report_configuration_outputs_input.deserialize_json(
                data["outputs"]
            )
        )
    if "dataSources" in data:
        import aws_sdk_fis.types.experiment_template_report_configuration_data_sources_input

        out["data_sources"] = (
            aws_sdk_fis.types.experiment_template_report_configuration_data_sources_input.deserialize_json(
                data["dataSources"]
            )
        )
    if "preExperimentDuration" in data:
        out["pre_experiment_duration"] = data["preExperimentDuration"]
    if "postExperimentDuration" in data:
        out["post_experiment_duration"] = data["postExperimentDuration"]
    return out
