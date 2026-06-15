"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateTrainingJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.profiler_config_for_update
    import aws_sdk_sagemaker.types.profiler_rule_configurations
    import aws_sdk_sagemaker.types.remote_debug_config_for_update
    import aws_sdk_sagemaker.types.resource_config_for_update
    import aws_sdk_sagemaker.types.training_job_name


class UpdateTrainingJobRequest(TypedDict):
    training_job_name: NotRequired[
        "aws_sdk_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of a training job to update the Debugger profiling configuration.</p>"""
    profiler_config: NotRequired[
        "aws_sdk_sagemaker.types.profiler_config_for_update.ProfilerConfigForUpdate"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger system monitoring, framework profiling, and storage paths.</p>"""
    profiler_rule_configurations: NotRequired[
        "aws_sdk_sagemaker.types.profiler_rule_configurations.ProfilerRuleConfigurations"
    ]
    """<p>Configuration information for Amazon SageMaker Debugger rules for profiling system and framework metrics.</p>"""
    resource_config: NotRequired[
        "aws_sdk_sagemaker.types.resource_config_for_update.ResourceConfigForUpdate"
    ]
    """<p>The training job <code>ResourceConfig</code> to update warm pool retention length.</p>"""
    remote_debug_config: NotRequired[
        "aws_sdk_sagemaker.types.remote_debug_config_for_update.RemoteDebugConfigForUpdate"
    ]
    r"""<p>Configuration for remote debugging while the training job is running. You can update the remote debugging configuration when the <code>SecondaryStatus</code> of the job is <code>Downloading</code> or <code>Training</code>.To learn more about the remote debugging functionality of SageMaker, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html\">Access a training container through Amazon Web Services Systems Manager (SSM) for remote debugging</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTrainingJobRequest) -> dict:
    out: dict = {}
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
    if "profiler_config" in value:
        import aws_sdk_sagemaker.types.profiler_config_for_update

        out["ProfilerConfig"] = (
            aws_sdk_sagemaker.types.profiler_config_for_update.serialize_aws_json_1_1(
                value["profiler_config"]
            )
        )
    if "profiler_rule_configurations" in value:
        import aws_sdk_sagemaker.types.profiler_rule_configurations

        out["ProfilerRuleConfigurations"] = (
            aws_sdk_sagemaker.types.profiler_rule_configurations.serialize_aws_json_1_1(
                value["profiler_rule_configurations"]
            )
        )
    if "resource_config" in value:
        import aws_sdk_sagemaker.types.resource_config_for_update

        out["ResourceConfig"] = (
            aws_sdk_sagemaker.types.resource_config_for_update.serialize_aws_json_1_1(
                value["resource_config"]
            )
        )
    if "remote_debug_config" in value:
        import aws_sdk_sagemaker.types.remote_debug_config_for_update

        out["RemoteDebugConfig"] = (
            aws_sdk_sagemaker.types.remote_debug_config_for_update.serialize_aws_json_1_1(
                value["remote_debug_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTrainingJobRequest:
    out: UpdateTrainingJobRequest = {}  # type: ignore[typeddict-item]
    if "TrainingJobName" in data:
        out["training_job_name"] = data["TrainingJobName"]
    if "ProfilerConfig" in data:
        import aws_sdk_sagemaker.types.profiler_config_for_update

        out["profiler_config"] = (
            aws_sdk_sagemaker.types.profiler_config_for_update.deserialize_aws_json_1_1(
                data["ProfilerConfig"]
            )
        )
    if "ProfilerRuleConfigurations" in data:
        import aws_sdk_sagemaker.types.profiler_rule_configurations

        out["profiler_rule_configurations"] = (
            aws_sdk_sagemaker.types.profiler_rule_configurations.deserialize_aws_json_1_1(
                data["ProfilerRuleConfigurations"]
            )
        )
    if "ResourceConfig" in data:
        import aws_sdk_sagemaker.types.resource_config_for_update

        out["resource_config"] = (
            aws_sdk_sagemaker.types.resource_config_for_update.deserialize_aws_json_1_1(
                data["ResourceConfig"]
            )
        )
    if "RemoteDebugConfig" in data:
        import aws_sdk_sagemaker.types.remote_debug_config_for_update

        out["remote_debug_config"] = (
            aws_sdk_sagemaker.types.remote_debug_config_for_update.deserialize_aws_json_1_1(
                data["RemoteDebugConfig"]
            )
        )
    return out
