"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobInputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.endpoint_input_configurations
    import aws_sdk_sagemaker.types.endpoints
    import aws_sdk_sagemaker.types.job_duration_in_seconds
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.model_package_arn
    import aws_sdk_sagemaker.types.recommendation_job_container_config
    import aws_sdk_sagemaker.types.recommendation_job_resource_limit
    import aws_sdk_sagemaker.types.recommendation_job_vpc_config
    import aws_sdk_sagemaker.types.traffic_pattern


class RecommendationJobInputConfig(TypedDict, closed=True):
    model_package_version_arn: NotRequired[
        "aws_sdk_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a versioned model package.</p>"""
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of the created model.</p>"""
    job_duration_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.job_duration_in_seconds.JobDurationInSeconds"
    ]
    """<p>Specifies the maximum duration of the job, in seconds. The maximum value is 18,000 seconds.</p>"""
    traffic_pattern: NotRequired[
        "aws_sdk_sagemaker.types.traffic_pattern.TrafficPattern"
    ]
    """<p>Specifies the traffic pattern of the job.</p>"""
    resource_limit: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_resource_limit.RecommendationJobResourceLimit"
    ]
    """<p>Defines the resource limit of the job.</p>"""
    endpoint_configurations: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_input_configurations.EndpointInputConfigurations"
    ]
    """<p>Specifies the endpoint configuration to use for a job.</p>"""
    volume_kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    r"""<p>The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service (Amazon Web Services KMS) key that Amazon SageMaker uses to encrypt data on the storage volume attached to the ML compute instance that hosts the endpoint. This key will be passed to SageMaker Hosting for endpoint creation. </p> <p>The SageMaker execution role must have <code>kms:CreateGrant</code> permission in order to encrypt data on the storage volume of the endpoints created for inference recommendation. The inference recommendation job will fail asynchronously during endpoint configuration creation if the role passed does not have <code>kms:CreateGrant</code> permission.</p> <p>The <code>KmsKeyId</code> can be any of the following formats:</p> <ul> <li> <p>// KMS Key ID</p> <p> <code>\"1234abcd-12ab-34cd-56ef-1234567890ab\"</code> </p> </li> <li> <p>// Amazon Resource Name (ARN) of a KMS Key</p> <p> <code>\"arn:aws:kms:&lt;region&gt;:&lt;account&gt;:key/&lt;key-id-12ab-34cd-56ef-1234567890ab&gt;\"</code> </p> </li> <li> <p>// KMS Key Alias</p> <p> <code>\"alias/ExampleAlias\"</code> </p> </li> <li> <p>// Amazon Resource Name (ARN) of a KMS Key Alias</p> <p> <code>\"arn:aws:kms:&lt;region&gt;:&lt;account&gt;:alias/&lt;ExampleAlias&gt;\"</code> </p> </li> </ul> <p>For more information about key identifiers, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id\">Key identifiers (KeyID)</a> in the Amazon Web Services Key Management Service (Amazon Web Services KMS) documentation.</p>"""
    container_config: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_container_config.RecommendationJobContainerConfig"
    ]
    """<p>Specifies mandatory fields for running an Inference Recommender job. The fields specified in <code>ContainerConfig</code> override the corresponding fields in the model package.</p>"""
    endpoints: NotRequired["aws_sdk_sagemaker.types.endpoints.Endpoints"]
    """<p>Existing customer endpoints on which to run an Inference Recommender job.</p>"""
    vpc_config: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_vpc_config.RecommendationJobVpcConfig"
    ]
    """<p>Inference Recommender provisions SageMaker endpoints with access to VPC in the inference recommendation job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobInputConfig) -> dict:
    out: dict = {}
    if "model_package_version_arn" in value:
        out["ModelPackageVersionArn"] = value["model_package_version_arn"]
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "job_duration_in_seconds" in value:
        out["JobDurationInSeconds"] = value["job_duration_in_seconds"]
    if "traffic_pattern" in value:
        import aws_sdk_sagemaker.types.traffic_pattern

        out["TrafficPattern"] = (
            aws_sdk_sagemaker.types.traffic_pattern.serialize_aws_json_1_1(
                value["traffic_pattern"]
            )
        )
    if "resource_limit" in value:
        import aws_sdk_sagemaker.types.recommendation_job_resource_limit

        out["ResourceLimit"] = (
            aws_sdk_sagemaker.types.recommendation_job_resource_limit.serialize_aws_json_1_1(
                value["resource_limit"]
            )
        )
    if "endpoint_configurations" in value:
        import aws_sdk_sagemaker.types.endpoint_input_configurations

        out["EndpointConfigurations"] = (
            aws_sdk_sagemaker.types.endpoint_input_configurations.serialize_aws_json_1_1(
                value["endpoint_configurations"]
            )
        )
    if "volume_kms_key_id" in value:
        out["VolumeKmsKeyId"] = value["volume_kms_key_id"]
    if "container_config" in value:
        import aws_sdk_sagemaker.types.recommendation_job_container_config

        out["ContainerConfig"] = (
            aws_sdk_sagemaker.types.recommendation_job_container_config.serialize_aws_json_1_1(
                value["container_config"]
            )
        )
    if "endpoints" in value:
        import aws_sdk_sagemaker.types.endpoints

        out["Endpoints"] = aws_sdk_sagemaker.types.endpoints.serialize_aws_json_1_1(
            value["endpoints"]
        )
    if "vpc_config" in value:
        import aws_sdk_sagemaker.types.recommendation_job_vpc_config

        out["VpcConfig"] = (
            aws_sdk_sagemaker.types.recommendation_job_vpc_config.serialize_aws_json_1_1(
                value["vpc_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobInputConfig:
    out: RecommendationJobInputConfig = {}  # type: ignore[typeddict-item]
    if "ModelPackageVersionArn" in data:
        out["model_package_version_arn"] = data["ModelPackageVersionArn"]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "JobDurationInSeconds" in data:
        out["job_duration_in_seconds"] = data["JobDurationInSeconds"]
    if "TrafficPattern" in data:
        import aws_sdk_sagemaker.types.traffic_pattern

        out["traffic_pattern"] = (
            aws_sdk_sagemaker.types.traffic_pattern.deserialize_aws_json_1_1(
                data["TrafficPattern"]
            )
        )
    if "ResourceLimit" in data:
        import aws_sdk_sagemaker.types.recommendation_job_resource_limit

        out["resource_limit"] = (
            aws_sdk_sagemaker.types.recommendation_job_resource_limit.deserialize_aws_json_1_1(
                data["ResourceLimit"]
            )
        )
    if "EndpointConfigurations" in data:
        import aws_sdk_sagemaker.types.endpoint_input_configurations

        out["endpoint_configurations"] = (
            aws_sdk_sagemaker.types.endpoint_input_configurations.deserialize_aws_json_1_1(
                data["EndpointConfigurations"]
            )
        )
    if "VolumeKmsKeyId" in data:
        out["volume_kms_key_id"] = data["VolumeKmsKeyId"]
    if "ContainerConfig" in data:
        import aws_sdk_sagemaker.types.recommendation_job_container_config

        out["container_config"] = (
            aws_sdk_sagemaker.types.recommendation_job_container_config.deserialize_aws_json_1_1(
                data["ContainerConfig"]
            )
        )
    if "Endpoints" in data:
        import aws_sdk_sagemaker.types.endpoints

        out["endpoints"] = aws_sdk_sagemaker.types.endpoints.deserialize_aws_json_1_1(
            data["Endpoints"]
        )
    if "VpcConfig" in data:
        import aws_sdk_sagemaker.types.recommendation_job_vpc_config

        out["vpc_config"] = (
            aws_sdk_sagemaker.types.recommendation_job_vpc_config.deserialize_aws_json_1_1(
                data["VpcConfig"]
            )
        )
    return out
