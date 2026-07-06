"""Generated from Smithy shape ``com.amazonaws.appconfig#StartDeploymentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.deployment_strategy_id
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.dynamic_parameter_map
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.kms_key_identifier
    import aws_sdk_appconfig.types.tag_map
    import aws_sdk_appconfig.types.version


class StartDeploymentRequest(TypedDict, closed=True):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    environment_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The environment ID.</p>"""
    deployment_strategy_id: (
        "aws_sdk_appconfig.types.deployment_strategy_id.DeploymentStrategyId"
    )
    """<p>The deployment strategy ID.</p>"""
    configuration_profile_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The configuration profile ID.</p>"""
    configuration_version: "aws_sdk_appconfig.types.version.Version"
    """<p>The configuration version to deploy. If deploying an AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>A description of the deployment.</p>"""
    tags: NotRequired["aws_sdk_appconfig.types.tag_map.TagMap"]
    """<p>Metadata to assign to the deployment. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The KMS key identifier (key ID, key alias, or key ARN). AppConfig uses this ID to encrypt the configuration data using a customer managed key. </p>"""
    dynamic_extension_parameters: NotRequired[
        "aws_sdk_appconfig.types.dynamic_parameter_map.DynamicParameterMap"
    ]
    """<p>A map of dynamic extension parameter names to values to pass to associated extensions with <code>PRE_START_DEPLOYMENT</code> actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDeploymentRequest) -> dict:
    out: dict = {}
    out["DeploymentStrategyId"] = value["deployment_strategy_id"]
    out["ConfigurationProfileId"] = value["configuration_profile_id"]
    out["ConfigurationVersion"] = value["configuration_version"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_appconfig.types.tag_map

        out["Tags"] = aws_sdk_appconfig.types.tag_map.serialize_json(value["tags"])
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "dynamic_extension_parameters" in value:
        import aws_sdk_appconfig.types.dynamic_parameter_map

        out["DynamicExtensionParameters"] = (
            aws_sdk_appconfig.types.dynamic_parameter_map.serialize_json(
                value["dynamic_extension_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartDeploymentRequest:
    out: StartDeploymentRequest = {}  # type: ignore[typeddict-item]
    if "DeploymentStrategyId" in data:
        out["deployment_strategy_id"] = data["DeploymentStrategyId"]
    else:
        raise DeserializationError(
            "StartDeploymentRequest.deployment_strategy_id required"
        )
    if "ConfigurationProfileId" in data:
        out["configuration_profile_id"] = data["ConfigurationProfileId"]
    else:
        raise DeserializationError(
            "StartDeploymentRequest.configuration_profile_id required"
        )
    if "ConfigurationVersion" in data:
        out["configuration_version"] = data["ConfigurationVersion"]
    else:
        raise DeserializationError(
            "StartDeploymentRequest.configuration_version required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_appconfig.types.tag_map

        out["tags"] = aws_sdk_appconfig.types.tag_map.deserialize_json(data["Tags"])
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if "DynamicExtensionParameters" in data:
        import aws_sdk_appconfig.types.dynamic_parameter_map

        out["dynamic_extension_parameters"] = (
            aws_sdk_appconfig.types.dynamic_parameter_map.deserialize_json(
                data["DynamicExtensionParameters"]
            )
        )
    return out
