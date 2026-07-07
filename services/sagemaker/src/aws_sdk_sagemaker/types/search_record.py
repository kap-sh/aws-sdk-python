"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint
    import aws_sdk_sagemaker.types.experiment
    import aws_sdk_sagemaker.types.feature_group
    import aws_sdk_sagemaker.types.feature_metadata
    import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_search_entity
    import aws_sdk_sagemaker.types.job
    import aws_sdk_sagemaker.types.model_card
    import aws_sdk_sagemaker.types.model_dashboard_model
    import aws_sdk_sagemaker.types.model_package
    import aws_sdk_sagemaker.types.model_package_group
    import aws_sdk_sagemaker.types.pipeline
    import aws_sdk_sagemaker.types.pipeline_execution
    import aws_sdk_sagemaker.types.pipeline_version
    import aws_sdk_sagemaker.types.project
    import aws_sdk_sagemaker.types.training_job
    import aws_sdk_sagemaker.types.trial
    import aws_sdk_sagemaker.types.trial_component


class SearchRecord(TypedDict, closed=True):
    training_job: NotRequired["aws_sdk_sagemaker.types.training_job.TrainingJob"]
    """<p>The properties of a training job.</p>"""
    experiment: NotRequired["aws_sdk_sagemaker.types.experiment.Experiment"]
    """<p>The properties of an experiment.</p>"""
    trial: NotRequired["aws_sdk_sagemaker.types.trial.Trial"]
    """<p>The properties of a trial.</p>"""
    trial_component: NotRequired[
        "aws_sdk_sagemaker.types.trial_component.TrialComponent"
    ]
    """<p>The properties of a trial component.</p>"""
    endpoint: NotRequired["aws_sdk_sagemaker.types.endpoint.Endpoint"]
    model_package: NotRequired["aws_sdk_sagemaker.types.model_package.ModelPackage"]
    model_package_group: NotRequired[
        "aws_sdk_sagemaker.types.model_package_group.ModelPackageGroup"
    ]
    pipeline: NotRequired["aws_sdk_sagemaker.types.pipeline.Pipeline"]
    pipeline_execution: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_execution.PipelineExecution"
    ]
    pipeline_version: NotRequired[
        "aws_sdk_sagemaker.types.pipeline_version.PipelineVersion"
    ]
    """<p>The version of the pipeline.</p>"""
    feature_group: NotRequired["aws_sdk_sagemaker.types.feature_group.FeatureGroup"]
    feature_metadata: NotRequired[
        "aws_sdk_sagemaker.types.feature_metadata.FeatureMetadata"
    ]
    """<p>The feature metadata used to search through the features.</p>"""
    project: NotRequired["aws_sdk_sagemaker.types.project.Project"]
    """<p>The properties of a project.</p>"""
    hyper_parameter_tuning_job: NotRequired[
        "aws_sdk_sagemaker.types.hyper_parameter_tuning_job_search_entity.HyperParameterTuningJobSearchEntity"
    ]
    """<p>The properties of a hyperparameter tuning job.</p>"""
    model_card: NotRequired["aws_sdk_sagemaker.types.model_card.ModelCard"]
    """<p>An Amazon SageMaker Model Card that documents details about a machine learning model.</p>"""
    model: NotRequired[
        "aws_sdk_sagemaker.types.model_dashboard_model.ModelDashboardModel"
    ]
    job: NotRequired["aws_sdk_sagemaker.types.job.Job"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchRecord) -> dict:
    out: dict = {}
    if "training_job" in value:
        import aws_sdk_sagemaker.types.training_job

        out["TrainingJob"] = (
            aws_sdk_sagemaker.types.training_job.serialize_aws_json_1_1(
                value["training_job"]
            )
        )
    if "experiment" in value:
        import aws_sdk_sagemaker.types.experiment

        out["Experiment"] = aws_sdk_sagemaker.types.experiment.serialize_aws_json_1_1(
            value["experiment"]
        )
    if "trial" in value:
        import aws_sdk_sagemaker.types.trial

        out["Trial"] = aws_sdk_sagemaker.types.trial.serialize_aws_json_1_1(
            value["trial"]
        )
    if "trial_component" in value:
        import aws_sdk_sagemaker.types.trial_component

        out["TrialComponent"] = (
            aws_sdk_sagemaker.types.trial_component.serialize_aws_json_1_1(
                value["trial_component"]
            )
        )
    if "endpoint" in value:
        import aws_sdk_sagemaker.types.endpoint

        out["Endpoint"] = aws_sdk_sagemaker.types.endpoint.serialize_aws_json_1_1(
            value["endpoint"]
        )
    if "model_package" in value:
        import aws_sdk_sagemaker.types.model_package

        out["ModelPackage"] = (
            aws_sdk_sagemaker.types.model_package.serialize_aws_json_1_1(
                value["model_package"]
            )
        )
    if "model_package_group" in value:
        import aws_sdk_sagemaker.types.model_package_group

        out["ModelPackageGroup"] = (
            aws_sdk_sagemaker.types.model_package_group.serialize_aws_json_1_1(
                value["model_package_group"]
            )
        )
    if "pipeline" in value:
        import aws_sdk_sagemaker.types.pipeline

        out["Pipeline"] = aws_sdk_sagemaker.types.pipeline.serialize_aws_json_1_1(
            value["pipeline"]
        )
    if "pipeline_execution" in value:
        import aws_sdk_sagemaker.types.pipeline_execution

        out["PipelineExecution"] = (
            aws_sdk_sagemaker.types.pipeline_execution.serialize_aws_json_1_1(
                value["pipeline_execution"]
            )
        )
    if "pipeline_version" in value:
        import aws_sdk_sagemaker.types.pipeline_version

        out["PipelineVersion"] = (
            aws_sdk_sagemaker.types.pipeline_version.serialize_aws_json_1_1(
                value["pipeline_version"]
            )
        )
    if "feature_group" in value:
        import aws_sdk_sagemaker.types.feature_group

        out["FeatureGroup"] = (
            aws_sdk_sagemaker.types.feature_group.serialize_aws_json_1_1(
                value["feature_group"]
            )
        )
    if "feature_metadata" in value:
        import aws_sdk_sagemaker.types.feature_metadata

        out["FeatureMetadata"] = (
            aws_sdk_sagemaker.types.feature_metadata.serialize_aws_json_1_1(
                value["feature_metadata"]
            )
        )
    if "project" in value:
        import aws_sdk_sagemaker.types.project

        out["Project"] = aws_sdk_sagemaker.types.project.serialize_aws_json_1_1(
            value["project"]
        )
    if "hyper_parameter_tuning_job" in value:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_search_entity

        out["HyperParameterTuningJob"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_search_entity.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job"]
            )
        )
    if "model_card" in value:
        import aws_sdk_sagemaker.types.model_card

        out["ModelCard"] = aws_sdk_sagemaker.types.model_card.serialize_aws_json_1_1(
            value["model_card"]
        )
    if "model" in value:
        import aws_sdk_sagemaker.types.model_dashboard_model

        out["Model"] = (
            aws_sdk_sagemaker.types.model_dashboard_model.serialize_aws_json_1_1(
                value["model"]
            )
        )
    if "job" in value:
        import aws_sdk_sagemaker.types.job

        out["Job"] = aws_sdk_sagemaker.types.job.serialize_aws_json_1_1(value["job"])
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchRecord:
    out: SearchRecord = {}  # type: ignore[typeddict-item]
    if "TrainingJob" in data:
        import aws_sdk_sagemaker.types.training_job

        out["training_job"] = (
            aws_sdk_sagemaker.types.training_job.deserialize_aws_json_1_1(
                data["TrainingJob"]
            )
        )
    if "Experiment" in data:
        import aws_sdk_sagemaker.types.experiment

        out["experiment"] = aws_sdk_sagemaker.types.experiment.deserialize_aws_json_1_1(
            data["Experiment"]
        )
    if "Trial" in data:
        import aws_sdk_sagemaker.types.trial

        out["trial"] = aws_sdk_sagemaker.types.trial.deserialize_aws_json_1_1(
            data["Trial"]
        )
    if "TrialComponent" in data:
        import aws_sdk_sagemaker.types.trial_component

        out["trial_component"] = (
            aws_sdk_sagemaker.types.trial_component.deserialize_aws_json_1_1(
                data["TrialComponent"]
            )
        )
    if "Endpoint" in data:
        import aws_sdk_sagemaker.types.endpoint

        out["endpoint"] = aws_sdk_sagemaker.types.endpoint.deserialize_aws_json_1_1(
            data["Endpoint"]
        )
    if "ModelPackage" in data:
        import aws_sdk_sagemaker.types.model_package

        out["model_package"] = (
            aws_sdk_sagemaker.types.model_package.deserialize_aws_json_1_1(
                data["ModelPackage"]
            )
        )
    if "ModelPackageGroup" in data:
        import aws_sdk_sagemaker.types.model_package_group

        out["model_package_group"] = (
            aws_sdk_sagemaker.types.model_package_group.deserialize_aws_json_1_1(
                data["ModelPackageGroup"]
            )
        )
    if "Pipeline" in data:
        import aws_sdk_sagemaker.types.pipeline

        out["pipeline"] = aws_sdk_sagemaker.types.pipeline.deserialize_aws_json_1_1(
            data["Pipeline"]
        )
    if "PipelineExecution" in data:
        import aws_sdk_sagemaker.types.pipeline_execution

        out["pipeline_execution"] = (
            aws_sdk_sagemaker.types.pipeline_execution.deserialize_aws_json_1_1(
                data["PipelineExecution"]
            )
        )
    if "PipelineVersion" in data:
        import aws_sdk_sagemaker.types.pipeline_version

        out["pipeline_version"] = (
            aws_sdk_sagemaker.types.pipeline_version.deserialize_aws_json_1_1(
                data["PipelineVersion"]
            )
        )
    if "FeatureGroup" in data:
        import aws_sdk_sagemaker.types.feature_group

        out["feature_group"] = (
            aws_sdk_sagemaker.types.feature_group.deserialize_aws_json_1_1(
                data["FeatureGroup"]
            )
        )
    if "FeatureMetadata" in data:
        import aws_sdk_sagemaker.types.feature_metadata

        out["feature_metadata"] = (
            aws_sdk_sagemaker.types.feature_metadata.deserialize_aws_json_1_1(
                data["FeatureMetadata"]
            )
        )
    if "Project" in data:
        import aws_sdk_sagemaker.types.project

        out["project"] = aws_sdk_sagemaker.types.project.deserialize_aws_json_1_1(
            data["Project"]
        )
    if "HyperParameterTuningJob" in data:
        import aws_sdk_sagemaker.types.hyper_parameter_tuning_job_search_entity

        out["hyper_parameter_tuning_job"] = (
            aws_sdk_sagemaker.types.hyper_parameter_tuning_job_search_entity.deserialize_aws_json_1_1(
                data["HyperParameterTuningJob"]
            )
        )
    if "ModelCard" in data:
        import aws_sdk_sagemaker.types.model_card

        out["model_card"] = aws_sdk_sagemaker.types.model_card.deserialize_aws_json_1_1(
            data["ModelCard"]
        )
    if "Model" in data:
        import aws_sdk_sagemaker.types.model_dashboard_model

        out["model"] = (
            aws_sdk_sagemaker.types.model_dashboard_model.deserialize_aws_json_1_1(
                data["Model"]
            )
        )
    if "Job" in data:
        import aws_sdk_sagemaker.types.job

        out["job"] = aws_sdk_sagemaker.types.job.deserialize_aws_json_1_1(data["Job"])
    return out
