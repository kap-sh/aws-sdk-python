"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateEndpointInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.deployment_config
    import aws_sdk_sagemaker.types.endpoint_config_name
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.variant_property_list


class UpdateEndpointInput(TypedDict):
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint whose configuration you want to update.</p>"""
    endpoint_config_name: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The name of the new endpoint configuration.</p>"""
    retain_all_variant_properties: NotRequired[
        "aws_sdk_sagemaker.types.boolean.Boolean"
    ]
    """<p>When updating endpoint resources, enables or disables the retention of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VariantProperty.html\">variant properties</a>, such as the instance count or the variant weight. To retain the variant properties of an endpoint when updating it, set <code>RetainAllVariantProperties</code> to <code>true</code>. To use the variant properties specified in a new <code>EndpointConfig</code> call when updating an endpoint, set <code>RetainAllVariantProperties</code> to <code>false</code>. The default is <code>false</code>.</p>"""
    exclude_retained_variant_properties: NotRequired[
        "aws_sdk_sagemaker.types.variant_property_list.VariantPropertyList"
    ]
    """<p>When you are updating endpoint resources with <code>RetainAllVariantProperties</code>, whose value is set to <code>true</code>, <code>ExcludeRetainedVariantProperties</code> specifies the list of type <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VariantProperty.html\">VariantProperty</a> to override with the values provided by <code>EndpointConfig</code>. If you don't specify a value for <code>ExcludeRetainedVariantProperties</code>, no variant properties are overridden. </p>"""
    deployment_config: NotRequired[
        "aws_sdk_sagemaker.types.deployment_config.DeploymentConfig"
    ]
    """<p>The deployment configuration for an endpoint, which contains the desired deployment strategy and rollback configurations.</p>"""
    retain_deployment_config: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Specifies whether to reuse the last deployment configuration. The default value is false (the configuration is not reused).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointInput) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "retain_all_variant_properties" in value:
        out["RetainAllVariantProperties"] = value["retain_all_variant_properties"]
    if "exclude_retained_variant_properties" in value:
        import aws_sdk_sagemaker.types.variant_property_list

        out["ExcludeRetainedVariantProperties"] = (
            aws_sdk_sagemaker.types.variant_property_list.serialize_aws_json_1_1(
                value["exclude_retained_variant_properties"]
            )
        )
    if "deployment_config" in value:
        import aws_sdk_sagemaker.types.deployment_config

        out["DeploymentConfig"] = (
            aws_sdk_sagemaker.types.deployment_config.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    if "retain_deployment_config" in value:
        out["RetainDeploymentConfig"] = value["retain_deployment_config"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointInput:
    out: UpdateEndpointInput = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "EndpointConfigName" in data:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if "RetainAllVariantProperties" in data:
        out["retain_all_variant_properties"] = data["RetainAllVariantProperties"]
    if "ExcludeRetainedVariantProperties" in data:
        import aws_sdk_sagemaker.types.variant_property_list

        out["exclude_retained_variant_properties"] = (
            aws_sdk_sagemaker.types.variant_property_list.deserialize_aws_json_1_1(
                data["ExcludeRetainedVariantProperties"]
            )
        )
    if "DeploymentConfig" in data:
        import aws_sdk_sagemaker.types.deployment_config

        out["deployment_config"] = (
            aws_sdk_sagemaker.types.deployment_config.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    if "RetainDeploymentConfig" in data:
        out["retain_deployment_config"] = data["RetainDeploymentConfig"]
    return out
