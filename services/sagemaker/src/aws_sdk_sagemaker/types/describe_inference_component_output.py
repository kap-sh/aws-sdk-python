"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeInferenceComponentOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_arn
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.inference_component_arn
    import aws_sdk_sagemaker.types.inference_component_deployment_config
    import aws_sdk_sagemaker.types.inference_component_name
    import aws_sdk_sagemaker.types.inference_component_runtime_config_summary
    import aws_sdk_sagemaker.types.inference_component_specification_summary
    import aws_sdk_sagemaker.types.inference_component_specification_summary_list
    import aws_sdk_sagemaker.types.inference_component_status
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.variant_name


class DescribeInferenceComponentOutput(TypedDict):
    inference_component_name: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_name.InferenceComponentName"
    ]
    """<p>The name of the inference component.</p>"""
    inference_component_arn: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_arn.InferenceComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference component.</p>"""
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint that hosts the inference component.</p>"""
    endpoint_arn: NotRequired["aws_sdk_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint that hosts the inference component.</p>"""
    variant_name: NotRequired["aws_sdk_sagemaker.types.variant_name.VariantName"]
    """<p>The name of the production variant that hosts the inference component.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the inference component status is <code>Failed</code>, the reason for the failure.</p>"""
    specification: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_specification_summary.InferenceComponentSpecificationSummary"
    ]
    """<p>Details about the resources that are deployed with this inference component.</p>"""
    specifications: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_specification_summary_list.InferenceComponentSpecificationSummaryList"
    ]
    """<p>A list of specification summaries for the inference component, one per instance type. This parameter is populated when the inference component was created with multiple specifications. When this parameter is populated, the singular <code>Specification</code> parameter is not returned.</p>"""
    runtime_config: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_runtime_config_summary.InferenceComponentRuntimeConfigSummary"
    ]
    """<p>Details about the runtime settings for the model that is deployed with the inference component.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the inference component was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the inference component was last updated.</p>"""
    inference_component_status: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_status.InferenceComponentStatus"
    ]
    """<p>The status of the inference component.</p>"""
    last_deployment_config: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_deployment_config.InferenceComponentDeploymentConfig"
    ]
    """<p>The deployment and rollback settings that you assigned to the inference component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInferenceComponentOutput) -> dict:
    out: dict = {}
    if "inference_component_name" in value:
        out["InferenceComponentName"] = value["inference_component_name"]
    if "inference_component_arn" in value:
        out["InferenceComponentArn"] = value["inference_component_arn"]
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "specification" in value:
        import aws_sdk_sagemaker.types.inference_component_specification_summary

        out["Specification"] = (
            aws_sdk_sagemaker.types.inference_component_specification_summary.serialize_aws_json_1_1(
                value["specification"]
            )
        )
    if "specifications" in value:
        import aws_sdk_sagemaker.types.inference_component_specification_summary_list

        out["Specifications"] = (
            aws_sdk_sagemaker.types.inference_component_specification_summary_list.serialize_aws_json_1_1(
                value["specifications"]
            )
        )
    if "runtime_config" in value:
        import aws_sdk_sagemaker.types.inference_component_runtime_config_summary

        out["RuntimeConfig"] = (
            aws_sdk_sagemaker.types.inference_component_runtime_config_summary.serialize_aws_json_1_1(
                value["runtime_config"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "inference_component_status" in value:
        import aws_sdk_sagemaker.types.inference_component_status

        out["InferenceComponentStatus"] = (
            aws_sdk_sagemaker.types.inference_component_status.serialize_aws_json_1_1(
                value["inference_component_status"]
            )
        )
    if "last_deployment_config" in value:
        import aws_sdk_sagemaker.types.inference_component_deployment_config

        out["LastDeploymentConfig"] = (
            aws_sdk_sagemaker.types.inference_component_deployment_config.serialize_aws_json_1_1(
                value["last_deployment_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInferenceComponentOutput:
    out: DescribeInferenceComponentOutput = {}  # type: ignore[typeddict-item]
    if "InferenceComponentName" in data:
        out["inference_component_name"] = data["InferenceComponentName"]
    if "InferenceComponentArn" in data:
        out["inference_component_arn"] = data["InferenceComponentArn"]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "EndpointArn" in data:
        out["endpoint_arn"] = data["EndpointArn"]
    if "VariantName" in data:
        out["variant_name"] = data["VariantName"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Specification" in data:
        import aws_sdk_sagemaker.types.inference_component_specification_summary

        out["specification"] = (
            aws_sdk_sagemaker.types.inference_component_specification_summary.deserialize_aws_json_1_1(
                data["Specification"]
            )
        )
    if "Specifications" in data:
        import aws_sdk_sagemaker.types.inference_component_specification_summary_list

        out["specifications"] = (
            aws_sdk_sagemaker.types.inference_component_specification_summary_list.deserialize_aws_json_1_1(
                data["Specifications"]
            )
        )
    if "RuntimeConfig" in data:
        import aws_sdk_sagemaker.types.inference_component_runtime_config_summary

        out["runtime_config"] = (
            aws_sdk_sagemaker.types.inference_component_runtime_config_summary.deserialize_aws_json_1_1(
                data["RuntimeConfig"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "InferenceComponentStatus" in data:
        import aws_sdk_sagemaker.types.inference_component_status

        out["inference_component_status"] = (
            aws_sdk_sagemaker.types.inference_component_status.deserialize_aws_json_1_1(
                data["InferenceComponentStatus"]
            )
        )
    if "LastDeploymentConfig" in data:
        import aws_sdk_sagemaker.types.inference_component_deployment_config

        out["last_deployment_config"] = (
            aws_sdk_sagemaker.types.inference_component_deployment_config.deserialize_aws_json_1_1(
                data["LastDeploymentConfig"]
            )
        )
    return out
