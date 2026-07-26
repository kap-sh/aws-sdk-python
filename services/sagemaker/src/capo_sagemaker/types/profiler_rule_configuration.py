"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProfilerRuleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.algorithm_image
    import capo_sagemaker.types.directory_path
    import capo_sagemaker.types.optional_volume_size_in_gb
    import capo_sagemaker.types.processing_instance_type
    import capo_sagemaker.types.rule_configuration_name
    import capo_sagemaker.types.rule_parameters
    import capo_sagemaker.types.s3_uri


class ProfilerRuleConfiguration(TypedDict, closed=True):
    rule_configuration_name: NotRequired[
        "capo_sagemaker.types.rule_configuration_name.RuleConfigurationName"
    ]
    """<p>The name of the rule configuration. It must be unique relative to other rule configuration names.</p>"""
    local_path: NotRequired["capo_sagemaker.types.directory_path.DirectoryPath"]
    """<p>Path to local storage location for output of rules. Defaults to <code>/opt/ml/processing/output/rule/</code>. </p>"""
    s3_output_path: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>Path to Amazon S3 storage location for rules.</p>"""
    rule_evaluator_image: NotRequired[
        "capo_sagemaker.types.algorithm_image.AlgorithmImage"
    ]
    """<p>The Amazon Elastic Container Registry Image for the managed rule evaluation.</p>"""
    instance_type: NotRequired[
        "capo_sagemaker.types.processing_instance_type.ProcessingInstanceType"
    ]
    """<p>The instance type to deploy a custom rule for profiling a training job.</p>"""
    volume_size_in_gb: NotRequired[
        "capo_sagemaker.types.optional_volume_size_in_gb.OptionalVolumeSizeInGB"
    ]
    """<p>The size, in GB, of the ML storage volume attached to the processing instance.</p>"""
    rule_parameters: NotRequired["capo_sagemaker.types.rule_parameters.RuleParameters"]
    """<p>Runtime configuration for rule container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilerRuleConfiguration) -> dict:
    out: dict = {}
    if "rule_configuration_name" in value:
        out["RuleConfigurationName"] = value["rule_configuration_name"]
    if "local_path" in value:
        out["LocalPath"] = value["local_path"]
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    if "rule_evaluator_image" in value:
        out["RuleEvaluatorImage"] = value["rule_evaluator_image"]
    if "instance_type" in value:
        import capo_sagemaker.types.processing_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.processing_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    if "rule_parameters" in value:
        import capo_sagemaker.types.rule_parameters

        out["RuleParameters"] = (
            capo_sagemaker.types.rule_parameters.serialize_aws_json_1_1(
                value["rule_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProfilerRuleConfiguration:
    out: ProfilerRuleConfiguration = {}  # type: ignore[typeddict-item]
    if "RuleConfigurationName" in data:
        out["rule_configuration_name"] = data["RuleConfigurationName"]
    if "LocalPath" in data:
        out["local_path"] = data["LocalPath"]
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    if "RuleEvaluatorImage" in data:
        out["rule_evaluator_image"] = data["RuleEvaluatorImage"]
    if "InstanceType" in data:
        import capo_sagemaker.types.processing_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.processing_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "VolumeSizeInGB" in data:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    if "RuleParameters" in data:
        import capo_sagemaker.types.rule_parameters

        out["rule_parameters"] = (
            capo_sagemaker.types.rule_parameters.deserialize_aws_json_1_1(
                data["RuleParameters"]
            )
        )
    return out
