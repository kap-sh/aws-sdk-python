"""Generated from Smithy shape ``com.amazonaws.sagemaker#EndpointInputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.environment_parameter_ranges
    import capo_sagemaker.types.inference_specification_name
    import capo_sagemaker.types.production_variant_instance_type
    import capo_sagemaker.types.production_variant_serverless_config


class EndpointInputConfiguration(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The instance types to use for the load test.</p>"""
    serverless_config: NotRequired[
        "capo_sagemaker.types.production_variant_serverless_config.ProductionVariantServerlessConfig"
    ]
    inference_specification_name: NotRequired[
        "capo_sagemaker.types.inference_specification_name.InferenceSpecificationName"
    ]
    """<p>The inference specification name in the model package version.</p>"""
    environment_parameter_ranges: NotRequired[
        "capo_sagemaker.types.environment_parameter_ranges.EnvironmentParameterRanges"
    ]
    """<p> The parameter you want to benchmark against.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointInputConfiguration) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "serverless_config" in value:
        import capo_sagemaker.types.production_variant_serverless_config

        out["ServerlessConfig"] = (
            capo_sagemaker.types.production_variant_serverless_config.serialize_aws_json_1_1(
                value["serverless_config"]
            )
        )
    if "inference_specification_name" in value:
        out["InferenceSpecificationName"] = value["inference_specification_name"]
    if "environment_parameter_ranges" in value:
        import capo_sagemaker.types.environment_parameter_ranges

        out["EnvironmentParameterRanges"] = (
            capo_sagemaker.types.environment_parameter_ranges.serialize_aws_json_1_1(
                value["environment_parameter_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointInputConfiguration:
    out: EndpointInputConfiguration = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import capo_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "ServerlessConfig" in data:
        import capo_sagemaker.types.production_variant_serverless_config

        out["serverless_config"] = (
            capo_sagemaker.types.production_variant_serverless_config.deserialize_aws_json_1_1(
                data["ServerlessConfig"]
            )
        )
    if "InferenceSpecificationName" in data:
        out["inference_specification_name"] = data["InferenceSpecificationName"]
    if "EnvironmentParameterRanges" in data:
        import capo_sagemaker.types.environment_parameter_ranges

        out["environment_parameter_ranges"] = (
            capo_sagemaker.types.environment_parameter_ranges.deserialize_aws_json_1_1(
                data["EnvironmentParameterRanges"]
            )
        )
    return out
