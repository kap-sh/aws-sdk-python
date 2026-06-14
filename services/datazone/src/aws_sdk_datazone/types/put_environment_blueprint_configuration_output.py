"""Generated from Smithy shape ``com.amazonaws.datazone#PutEnvironmentBlueprintConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.enabled_region_list
    import aws_sdk_datazone.types.environment_blueprint_id
    import aws_sdk_datazone.types.policy_arn
    import aws_sdk_datazone.types.provisioning_configuration_list
    import aws_sdk_datazone.types.regional_parameter_map
    import aws_sdk_datazone.types.resource_configurations
    import aws_sdk_datazone.types.role_arn


class PutEnvironmentBlueprintConfigurationOutput(TypedDict):
    domain_id: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain.</p>"""
    environment_blueprint_id: (
        "aws_sdk_datazone.types.environment_blueprint_id.EnvironmentBlueprintId"
    )
    """<p>The identifier of the environment blueprint.</p>"""
    provisioning_role_arn: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>The ARN of the provisioning role.</p>"""
    environment_role_permission_boundary: NotRequired[
        "aws_sdk_datazone.types.policy_arn.PolicyArn"
    ]
    """<p>The environment role permissions boundary.</p>"""
    manage_access_role_arn: NotRequired["aws_sdk_datazone.types.role_arn.RoleArn"]
    """<p>The ARN of the manage access role.</p>"""
    enabled_regions: NotRequired[
        "aws_sdk_datazone.types.enabled_region_list.EnabledRegionList"
    ]
    """<p>Specifies the enabled Amazon Web Services Regions.</p>"""
    regional_parameters: NotRequired[
        "aws_sdk_datazone.types.regional_parameter_map.RegionalParameterMap"
    ]
    """<p>The regional parameters in the environment blueprint.</p>"""
    allow_user_provided_configurations: NotRequired["bool"]
    """<p>Specifies whether user-provided resource configurations are allowed for the environment blueprint.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment blueprint was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the environment blueprint was updated.</p>"""
    resource_configurations: NotRequired[
        "aws_sdk_datazone.types.resource_configurations.ResourceConfigurations"
    ]
    """<p>The resource configurations of the environment blueprint.</p>"""
    provisioning_configurations: NotRequired[
        "aws_sdk_datazone.types.provisioning_configuration_list.ProvisioningConfigurationList"
    ]
    """<p>The provisioning configuration of a blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutEnvironmentBlueprintConfigurationOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["environmentBlueprintId"] = value["environment_blueprint_id"]
    if "provisioning_role_arn" in value:
        out["provisioningRoleArn"] = value["provisioning_role_arn"]
    if "environment_role_permission_boundary" in value:
        out["environmentRolePermissionBoundary"] = value[
            "environment_role_permission_boundary"
        ]
    if "manage_access_role_arn" in value:
        out["manageAccessRoleArn"] = value["manage_access_role_arn"]
    if "enabled_regions" in value:
        import aws_sdk_datazone.types.enabled_region_list

        out["enabledRegions"] = (
            aws_sdk_datazone.types.enabled_region_list.serialize_json(
                value["enabled_regions"]
            )
        )
    if "regional_parameters" in value:
        import aws_sdk_datazone.types.regional_parameter_map

        out["regionalParameters"] = (
            aws_sdk_datazone.types.regional_parameter_map.serialize_json(
                value["regional_parameters"]
            )
        )
    if "allow_user_provided_configurations" in value:
        out["allowUserProvidedConfigurations"] = value[
            "allow_user_provided_configurations"
        ]
    if "created_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["createdAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["updatedAt"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "resource_configurations" in value:
        import aws_sdk_datazone.types.resource_configurations

        out["resourceConfigurations"] = (
            aws_sdk_datazone.types.resource_configurations.serialize_json(
                value["resource_configurations"]
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


def deserialize_json(data: dict) -> PutEnvironmentBlueprintConfigurationOutput:
    out: PutEnvironmentBlueprintConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    else:
        raise DeserializationError(
            "PutEnvironmentBlueprintConfigurationOutput.domain_id required"
        )
    if "environmentBlueprintId" in data:
        out["environment_blueprint_id"] = data["environmentBlueprintId"]
    else:
        raise DeserializationError(
            "PutEnvironmentBlueprintConfigurationOutput.environment_blueprint_id required"
        )
    if "provisioningRoleArn" in data:
        out["provisioning_role_arn"] = data["provisioningRoleArn"]
    if "environmentRolePermissionBoundary" in data:
        out["environment_role_permission_boundary"] = data[
            "environmentRolePermissionBoundary"
        ]
    if "manageAccessRoleArn" in data:
        out["manage_access_role_arn"] = data["manageAccessRoleArn"]
    if "enabledRegions" in data:
        import aws_sdk_datazone.types.enabled_region_list

        out["enabled_regions"] = (
            aws_sdk_datazone.types.enabled_region_list.deserialize_json(
                data["enabledRegions"]
            )
        )
    if "regionalParameters" in data:
        import aws_sdk_datazone.types.regional_parameter_map

        out["regional_parameters"] = (
            aws_sdk_datazone.types.regional_parameter_map.deserialize_json(
                data["regionalParameters"]
            )
        )
    if "allowUserProvidedConfigurations" in data:
        out["allow_user_provided_configurations"] = data[
            "allowUserProvidedConfigurations"
        ]
    if "createdAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["created_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["updated_at"] = aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "resourceConfigurations" in data:
        import aws_sdk_datazone.types.resource_configurations

        out["resource_configurations"] = (
            aws_sdk_datazone.types.resource_configurations.deserialize_json(
                data["resourceConfigurations"]
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
