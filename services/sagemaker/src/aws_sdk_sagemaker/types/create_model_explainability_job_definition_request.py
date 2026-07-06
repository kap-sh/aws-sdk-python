"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelExplainabilityJobDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_explainability_app_specification
    import aws_sdk_sagemaker.types.model_explainability_baseline_config
    import aws_sdk_sagemaker.types.model_explainability_job_input
    import aws_sdk_sagemaker.types.monitoring_job_definition_name
    import aws_sdk_sagemaker.types.monitoring_network_config
    import aws_sdk_sagemaker.types.monitoring_output_config
    import aws_sdk_sagemaker.types.monitoring_resources
    import aws_sdk_sagemaker.types.monitoring_stopping_condition
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.tag_list


class CreateModelExplainabilityJobDefinitionRequest(TypedDict, closed=True):
    job_definition_name: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_job_definition_name.MonitoringJobDefinitionName"
    ]
    """<p> The name of the model explainability job definition. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""
    model_explainability_baseline_config: NotRequired[
        "aws_sdk_sagemaker.types.model_explainability_baseline_config.ModelExplainabilityBaselineConfig"
    ]
    """<p>The baseline configuration for a model explainability job.</p>"""
    model_explainability_app_specification: NotRequired[
        "aws_sdk_sagemaker.types.model_explainability_app_specification.ModelExplainabilityAppSpecification"
    ]
    """<p>Configures the model explainability job to run a specified Docker container image.</p>"""
    model_explainability_job_input: NotRequired[
        "aws_sdk_sagemaker.types.model_explainability_job_input.ModelExplainabilityJobInput"
    ]
    """<p>Inputs for the model explainability job.</p>"""
    model_explainability_job_output_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_output_config.MonitoringOutputConfig"
    ]
    job_resources: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_resources.MonitoringResources"
    ]
    network_config: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_network_config.MonitoringNetworkConfig"
    ]
    """<p>Networking options for a model explainability job.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker AI can assume to perform tasks on your behalf.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_stopping_condition.MonitoringStoppingCondition"
    ]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>(Optional) An array of key-value pairs. For more information, see <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL\"> Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: CreateModelExplainabilityJobDefinitionRequest,
) -> dict:
    out: dict = {}
    if "job_definition_name" in value:
        out["JobDefinitionName"] = value["job_definition_name"]
    if "model_explainability_baseline_config" in value:
        import aws_sdk_sagemaker.types.model_explainability_baseline_config

        out["ModelExplainabilityBaselineConfig"] = (
            aws_sdk_sagemaker.types.model_explainability_baseline_config.serialize_aws_json_1_1(
                value["model_explainability_baseline_config"]
            )
        )
    if "model_explainability_app_specification" in value:
        import aws_sdk_sagemaker.types.model_explainability_app_specification

        out["ModelExplainabilityAppSpecification"] = (
            aws_sdk_sagemaker.types.model_explainability_app_specification.serialize_aws_json_1_1(
                value["model_explainability_app_specification"]
            )
        )
    if "model_explainability_job_input" in value:
        import aws_sdk_sagemaker.types.model_explainability_job_input

        out["ModelExplainabilityJobInput"] = (
            aws_sdk_sagemaker.types.model_explainability_job_input.serialize_aws_json_1_1(
                value["model_explainability_job_input"]
            )
        )
    if "model_explainability_job_output_config" in value:
        import aws_sdk_sagemaker.types.monitoring_output_config

        out["ModelExplainabilityJobOutputConfig"] = (
            aws_sdk_sagemaker.types.monitoring_output_config.serialize_aws_json_1_1(
                value["model_explainability_job_output_config"]
            )
        )
    if "job_resources" in value:
        import aws_sdk_sagemaker.types.monitoring_resources

        out["JobResources"] = (
            aws_sdk_sagemaker.types.monitoring_resources.serialize_aws_json_1_1(
                value["job_resources"]
            )
        )
    if "network_config" in value:
        import aws_sdk_sagemaker.types.monitoring_network_config

        out["NetworkConfig"] = (
            aws_sdk_sagemaker.types.monitoring_network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "stopping_condition" in value:
        import aws_sdk_sagemaker.types.monitoring_stopping_condition

        out["StoppingCondition"] = (
            aws_sdk_sagemaker.types.monitoring_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateModelExplainabilityJobDefinitionRequest:
    out: CreateModelExplainabilityJobDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "JobDefinitionName" in data:
        out["job_definition_name"] = data["JobDefinitionName"]
    if "ModelExplainabilityBaselineConfig" in data:
        import aws_sdk_sagemaker.types.model_explainability_baseline_config

        out["model_explainability_baseline_config"] = (
            aws_sdk_sagemaker.types.model_explainability_baseline_config.deserialize_aws_json_1_1(
                data["ModelExplainabilityBaselineConfig"]
            )
        )
    if "ModelExplainabilityAppSpecification" in data:
        import aws_sdk_sagemaker.types.model_explainability_app_specification

        out["model_explainability_app_specification"] = (
            aws_sdk_sagemaker.types.model_explainability_app_specification.deserialize_aws_json_1_1(
                data["ModelExplainabilityAppSpecification"]
            )
        )
    if "ModelExplainabilityJobInput" in data:
        import aws_sdk_sagemaker.types.model_explainability_job_input

        out["model_explainability_job_input"] = (
            aws_sdk_sagemaker.types.model_explainability_job_input.deserialize_aws_json_1_1(
                data["ModelExplainabilityJobInput"]
            )
        )
    if "ModelExplainabilityJobOutputConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_output_config

        out["model_explainability_job_output_config"] = (
            aws_sdk_sagemaker.types.monitoring_output_config.deserialize_aws_json_1_1(
                data["ModelExplainabilityJobOutputConfig"]
            )
        )
    if "JobResources" in data:
        import aws_sdk_sagemaker.types.monitoring_resources

        out["job_resources"] = (
            aws_sdk_sagemaker.types.monitoring_resources.deserialize_aws_json_1_1(
                data["JobResources"]
            )
        )
    if "NetworkConfig" in data:
        import aws_sdk_sagemaker.types.monitoring_network_config

        out["network_config"] = (
            aws_sdk_sagemaker.types.monitoring_network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "StoppingCondition" in data:
        import aws_sdk_sagemaker.types.monitoring_stopping_condition

        out["stopping_condition"] = (
            aws_sdk_sagemaker.types.monitoring_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
