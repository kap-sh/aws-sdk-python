"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointOutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.initial_instance_count
    import aws_sdk_sagemaker.types.production_variant_instance_type
    import aws_sdk_sagemaker.types.production_variant_serverless_config
    import aws_sdk_sagemaker.types.string


class EndpointOutputConfiguration(TypedDict, closed=True):
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name of the endpoint made during a recommendation job.</p>"""
    variant_name: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name of the production variant (deployed model) made during a recommendation job.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The instance type recommended by Amazon SageMaker Inference Recommender.</p>"""
    initial_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.initial_instance_count.InitialInstanceCount"
    ]
    """<p>The number of instances recommended to launch initially.</p>"""
    serverless_config: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_serverless_config.ProductionVariantServerlessConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointOutputConfiguration) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "variant_name" in value:
        out["VariantName"] = value["variant_name"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "initial_instance_count" in value:
        out["InitialInstanceCount"] = value["initial_instance_count"]
    if "serverless_config" in value:
        import aws_sdk_sagemaker.types.production_variant_serverless_config

        out["ServerlessConfig"] = (
            aws_sdk_sagemaker.types.production_variant_serverless_config.serialize_aws_json_1_1(
                value["serverless_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointOutputConfiguration:
    out: EndpointOutputConfiguration = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "VariantName" in data:
        out["variant_name"] = data["VariantName"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "InitialInstanceCount" in data:
        out["initial_instance_count"] = data["InitialInstanceCount"]
    if "ServerlessConfig" in data:
        import aws_sdk_sagemaker.types.production_variant_serverless_config

        out["serverless_config"] = (
            aws_sdk_sagemaker.types.production_variant_serverless_config.deserialize_aws_json_1_1(
                data["ServerlessConfig"]
            )
        )
    return out
