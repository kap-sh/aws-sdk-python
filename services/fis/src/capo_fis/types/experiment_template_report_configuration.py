"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateReportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_report_configuration_data_sources
    import capo_fis.types.experiment_template_report_configuration_outputs
    import capo_fis.types.report_configuration_duration


class ExperimentTemplateReportConfiguration(TypedDict, closed=True):
    outputs: NotRequired[
        "capo_fis.types.experiment_template_report_configuration_outputs.ExperimentTemplateReportConfigurationOutputs"
    ]
    """<p>Describes the output destinations of the experiment report.</p>"""
    data_sources: NotRequired[
        "capo_fis.types.experiment_template_report_configuration_data_sources.ExperimentTemplateReportConfigurationDataSources"
    ]
    """<p>The data sources for the experiment report.</p>"""
    pre_experiment_duration: NotRequired[
        "capo_fis.types.report_configuration_duration.ReportConfigurationDuration"
    ]
    """<p>The duration before the experiment start time for the data sources to include in the report.</p>"""
    post_experiment_duration: NotRequired[
        "capo_fis.types.report_configuration_duration.ReportConfigurationDuration"
    ]
    """<p>The duration after the experiment end time for the data sources to include in the report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTemplateReportConfiguration) -> dict:
    out: dict = {}
    if "outputs" in value:
        import capo_fis.types.experiment_template_report_configuration_outputs

        out["outputs"] = (
            capo_fis.types.experiment_template_report_configuration_outputs.serialize_json(
                value["outputs"]
            )
        )
    if "data_sources" in value:
        import capo_fis.types.experiment_template_report_configuration_data_sources

        out["dataSources"] = (
            capo_fis.types.experiment_template_report_configuration_data_sources.serialize_json(
                value["data_sources"]
            )
        )
    if "pre_experiment_duration" in value:
        out["preExperimentDuration"] = value["pre_experiment_duration"]
    if "post_experiment_duration" in value:
        out["postExperimentDuration"] = value["post_experiment_duration"]
    return out


def deserialize_json(data: dict) -> ExperimentTemplateReportConfiguration:
    out: ExperimentTemplateReportConfiguration = {}  # type: ignore[typeddict-item]
    if "outputs" in data:
        import capo_fis.types.experiment_template_report_configuration_outputs

        out["outputs"] = (
            capo_fis.types.experiment_template_report_configuration_outputs.deserialize_json(
                data["outputs"]
            )
        )
    if "dataSources" in data:
        import capo_fis.types.experiment_template_report_configuration_data_sources

        out["data_sources"] = (
            capo_fis.types.experiment_template_report_configuration_data_sources.deserialize_json(
                data["dataSources"]
            )
        )
    if "preExperimentDuration" in data:
        out["pre_experiment_duration"] = data["preExperimentDuration"]
    if "postExperimentDuration" in data:
        out["post_experiment_duration"] = data["postExperimentDuration"]
    return out
