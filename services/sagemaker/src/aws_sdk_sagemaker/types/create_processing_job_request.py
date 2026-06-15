"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateProcessingJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_specification
    import aws_sdk_sagemaker.types.experiment_config
    import aws_sdk_sagemaker.types.network_config
    import aws_sdk_sagemaker.types.processing_environment_map
    import aws_sdk_sagemaker.types.processing_inputs
    import aws_sdk_sagemaker.types.processing_job_name
    import aws_sdk_sagemaker.types.processing_output_config
    import aws_sdk_sagemaker.types.processing_resources
    import aws_sdk_sagemaker.types.processing_stopping_condition
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.tag_list


class CreateProcessingJobRequest(TypedDict):
    processing_inputs: NotRequired[
        "aws_sdk_sagemaker.types.processing_inputs.ProcessingInputs"
    ]
    """<p>An array of inputs configuring the data to download into the processing container.</p>"""
    processing_output_config: NotRequired[
        "aws_sdk_sagemaker.types.processing_output_config.ProcessingOutputConfig"
    ]
    """<p>Output configuration for the processing job.</p>"""
    processing_job_name: NotRequired[
        "aws_sdk_sagemaker.types.processing_job_name.ProcessingJobName"
    ]
    """<p> The name of the processing job. The name must be unique within an Amazon Web Services Region in the Amazon Web Services account.</p>"""
    processing_resources: NotRequired[
        "aws_sdk_sagemaker.types.processing_resources.ProcessingResources"
    ]
    """<p>Identifies the resources, ML compute instances, and ML storage volumes to deploy for a processing job. In distributed training, you specify more than one instance.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.processing_stopping_condition.ProcessingStoppingCondition"
    ]
    """<p>The time limit for how long the processing job is allowed to run.</p>"""
    app_specification: NotRequired[
        "aws_sdk_sagemaker.types.app_specification.AppSpecification"
    ]
    """<p>Configures the processing job to run a specified Docker container image.</p>"""
    environment: NotRequired[
        "aws_sdk_sagemaker.types.processing_environment_map.ProcessingEnvironmentMap"
    ]
    """<p>The environment variables to set in the Docker container. Up to 100 key and values entries in the map are supported.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any environment fields. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request environment variable or plain text fields.</p> </important>"""
    network_config: NotRequired["aws_sdk_sagemaker.types.network_config.NetworkConfig"]
    """<p>Networking options for a processing job, such as whether to allow inbound and outbound network calls to and from processing containers, and the VPC subnets and security groups to use for VPC-enabled processing jobs.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>(Optional) An array of key-value pairs. For more information, see <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL\">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p> <important> <p>Do not include any security-sensitive information including account access IDs, secrets, or tokens in any tags. As part of the shared responsibility model, you are responsible for any potential exposure, unauthorized access, or compromise of your sensitive data if caused by security-sensitive information included in the request tag variable or plain text fields.</p> </important>"""
    experiment_config: NotRequired[
        "aws_sdk_sagemaker.types.experiment_config.ExperimentConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProcessingJobRequest) -> dict:
    out: dict = {}
    if "processing_inputs" in value:
        import aws_sdk_sagemaker.types.processing_inputs

        out["ProcessingInputs"] = (
            aws_sdk_sagemaker.types.processing_inputs.serialize_aws_json_1_1(
                value["processing_inputs"]
            )
        )
    if "processing_output_config" in value:
        import aws_sdk_sagemaker.types.processing_output_config

        out["ProcessingOutputConfig"] = (
            aws_sdk_sagemaker.types.processing_output_config.serialize_aws_json_1_1(
                value["processing_output_config"]
            )
        )
    if "processing_job_name" in value:
        out["ProcessingJobName"] = value["processing_job_name"]
    if "processing_resources" in value:
        import aws_sdk_sagemaker.types.processing_resources

        out["ProcessingResources"] = (
            aws_sdk_sagemaker.types.processing_resources.serialize_aws_json_1_1(
                value["processing_resources"]
            )
        )
    if "stopping_condition" in value:
        import aws_sdk_sagemaker.types.processing_stopping_condition

        out["StoppingCondition"] = (
            aws_sdk_sagemaker.types.processing_stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "app_specification" in value:
        import aws_sdk_sagemaker.types.app_specification

        out["AppSpecification"] = (
            aws_sdk_sagemaker.types.app_specification.serialize_aws_json_1_1(
                value["app_specification"]
            )
        )
    if "environment" in value:
        import aws_sdk_sagemaker.types.processing_environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.processing_environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "network_config" in value:
        import aws_sdk_sagemaker.types.network_config

        out["NetworkConfig"] = (
            aws_sdk_sagemaker.types.network_config.serialize_aws_json_1_1(
                value["network_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "experiment_config" in value:
        import aws_sdk_sagemaker.types.experiment_config

        out["ExperimentConfig"] = (
            aws_sdk_sagemaker.types.experiment_config.serialize_aws_json_1_1(
                value["experiment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProcessingJobRequest:
    out: CreateProcessingJobRequest = {}  # type: ignore[typeddict-item]
    if "ProcessingInputs" in data:
        import aws_sdk_sagemaker.types.processing_inputs

        out["processing_inputs"] = (
            aws_sdk_sagemaker.types.processing_inputs.deserialize_aws_json_1_1(
                data["ProcessingInputs"]
            )
        )
    if "ProcessingOutputConfig" in data:
        import aws_sdk_sagemaker.types.processing_output_config

        out["processing_output_config"] = (
            aws_sdk_sagemaker.types.processing_output_config.deserialize_aws_json_1_1(
                data["ProcessingOutputConfig"]
            )
        )
    if "ProcessingJobName" in data:
        out["processing_job_name"] = data["ProcessingJobName"]
    if "ProcessingResources" in data:
        import aws_sdk_sagemaker.types.processing_resources

        out["processing_resources"] = (
            aws_sdk_sagemaker.types.processing_resources.deserialize_aws_json_1_1(
                data["ProcessingResources"]
            )
        )
    if "StoppingCondition" in data:
        import aws_sdk_sagemaker.types.processing_stopping_condition

        out["stopping_condition"] = (
            aws_sdk_sagemaker.types.processing_stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if "AppSpecification" in data:
        import aws_sdk_sagemaker.types.app_specification

        out["app_specification"] = (
            aws_sdk_sagemaker.types.app_specification.deserialize_aws_json_1_1(
                data["AppSpecification"]
            )
        )
    if "Environment" in data:
        import aws_sdk_sagemaker.types.processing_environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.processing_environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    if "NetworkConfig" in data:
        import aws_sdk_sagemaker.types.network_config

        out["network_config"] = (
            aws_sdk_sagemaker.types.network_config.deserialize_aws_json_1_1(
                data["NetworkConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "ExperimentConfig" in data:
        import aws_sdk_sagemaker.types.experiment_config

        out["experiment_config"] = (
            aws_sdk_sagemaker.types.experiment_config.deserialize_aws_json_1_1(
                data["ExperimentConfig"]
            )
        )
    return out
