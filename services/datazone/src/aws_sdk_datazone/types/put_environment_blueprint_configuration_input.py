"""Generated from Smithy shape ``com.amazonaws.datazone#PutEnvironmentBlueprintConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.enabled_region_list
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.global_parameter_map
    import aws_sdk_datazone.types.policy_arn
    import aws_sdk_datazone.types.provisioning_configuration_list
    import aws_sdk_datazone.types.put_resource_configurations
    import aws_sdk_datazone.types.regional_parameter_map
    import aws_sdk_datazone.types.role_arn


class PutEnvironmentBlueprintConfigurationInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    environment_blueprint_identifier: (
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The identifier of the environment blueprint.</p>"""
    provisioning_role_arn: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>The ARN of the provisioning role.</p>"""
    manage_access_role_arn: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>The ARN of the manage access role.</p>"""
    environment_role_permission_boundary: NotRequired[
        "aws_sdk_datazone.types.policy_arn.PolicyArn"
    ]
    """<p>The environment role permissions boundary.</p>"""
    enabled_regions: "aws_sdk_datazone.types.enabled_region_list.EnabledRegionList"
    """<p>Specifies the enabled Amazon Web Services Regions.</p>"""
    regional_parameters: NotRequired[
        "aws_sdk_datazone.types.regional_parameter_map.RegionalParameterMap"
    ]
    """<p>The regional parameters in the environment blueprint.</p>"""
    resource_configurations: NotRequired[
        "aws_sdk_datazone.types.put_resource_configurations.PutResourceConfigurations"
    ]
    """<p>The resource configurations of the environment blueprint.</p>"""
    allow_user_provided_configurations: NotRequired["bool"]
    """<p>Specifies whether user-provided resource configurations are allowed for the environment blueprint.</p>"""
    global_parameters: NotRequired[
        "aws_sdk_datazone.types.global_parameter_map.GlobalParameterMap"
    ]
    """<p>Region-agnostic environment blueprint parameters. </p>"""
    provisioning_configurations: NotRequired[
        "aws_sdk_datazone.types.provisioning_configuration_list.ProvisioningConfigurationList"
    ]
    """<p>The provisioning configuration of a blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEnvironmentBlueprintConfigurationInput) -> dict:
    out: dict = {}
    if "provisioning_role_arn" in value:
        out["provisioningRoleArn"] = value["provisioning_role_arn"]
    if "manage_access_role_arn" in value:
        out["manageAccessRoleArn"] = value["manage_access_role_arn"]
    if "environment_role_permission_boundary" in value:
        out["environmentRolePermissionBoundary"] = value[
            "environment_role_permission_boundary"
        ]
    import aws_sdk_datazone.types.enabled_region_list

    out["enabledRegions"] = aws_sdk_datazone.types.enabled_region_list.serialize_json(
        value["enabled_regions"]
    )
    if "regional_parameters" in value:
        import aws_sdk_datazone.types.regional_parameter_map

        out["regionalParameters"] = (
            aws_sdk_datazone.types.regional_parameter_map.serialize_json(
                value["regional_parameters"]
            )
        )
    if "resource_configurations" in value:
        import aws_sdk_datazone.types.put_resource_configurations

        out["resourceConfigurations"] = (
            aws_sdk_datazone.types.put_resource_configurations.serialize_json(
                value["resource_configurations"]
            )
        )
    if "allow_user_provided_configurations" in value:
        out["allowUserProvidedConfigurations"] = value[
            "allow_user_provided_configurations"
        ]
    if "global_parameters" in value:
        import aws_sdk_datazone.types.global_parameter_map

        out["globalParameters"] = (
            aws_sdk_datazone.types.global_parameter_map.serialize_json(
                value["global_parameters"]
            )
        )
    if "provisioning_configurations" in value:
        import aws_sdk_datazone.types.provisioning_configuration_list

        out["provisioningConfigurations"] = (
            aws_sdk_datazone.types.provisioning_configuration_list.serialize_json(
                value["provisioning_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutEnvironmentBlueprintConfigurationInput:
    out: PutEnvironmentBlueprintConfigurationInput = {}  # type: ignore[typeddict-item]
    if "provisioningRoleArn" in data:
        out["provisioning_role_arn"] = data["provisioningRoleArn"]
    if "manageAccessRoleArn" in data:
        out["manage_access_role_arn"] = data["manageAccessRoleArn"]
    if "environmentRolePermissionBoundary" in data:
        out["environment_role_permission_boundary"] = data[
            "environmentRolePermissionBoundary"
        ]
    if "enabledRegions" in data:
        import aws_sdk_datazone.types.enabled_region_list

        out["enabled_regions"] = (
            aws_sdk_datazone.types.enabled_region_list.deserialize_json(
                data["enabledRegions"]
            )
        )
    else:
        raise DeserializationError(
            "PutEnvironmentBlueprintConfigurationInput.enabled_regions required"
        )
    if "regionalParameters" in data:
        import aws_sdk_datazone.types.regional_parameter_map

        out["regional_parameters"] = (
            aws_sdk_datazone.types.regional_parameter_map.deserialize_json(
                data["regionalParameters"]
            )
        )
    if "resourceConfigurations" in data:
        import aws_sdk_datazone.types.put_resource_configurations

        out["resource_configurations"] = (
            aws_sdk_datazone.types.put_resource_configurations.deserialize_json(
                data["resourceConfigurations"]
            )
        )
    if "allowUserProvidedConfigurations" in data:
        out["allow_user_provided_configurations"] = data[
            "allowUserProvidedConfigurations"
        ]
    if "globalParameters" in data:
        import aws_sdk_datazone.types.global_parameter_map

        out["global_parameters"] = (
            aws_sdk_datazone.types.global_parameter_map.deserialize_json(
                data["globalParameters"]
            )
        )
    if "provisioningConfigurations" in data:
        import aws_sdk_datazone.types.provisioning_configuration_list

        out["provisioning_configurations"] = (
            aws_sdk_datazone.types.provisioning_configuration_list.deserialize_json(
                data["provisioningConfigurations"]
            )
        )
    return out
