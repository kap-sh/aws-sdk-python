"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#LicenseSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.license_configuration_request

LicenseSpecifications: TypeAlias = list[
    "capo_workspaces_instances.types.license_configuration_request.LicenseConfigurationRequest"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseSpecifications) -> list:
    import capo_workspaces_instances.types.license_configuration_request

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.license_configuration_request.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseSpecifications:
    import capo_workspaces_instances.types.license_configuration_request

    out: LicenseSpecifications = []
    for item in data:
        out.append(
            capo_workspaces_instances.types.license_configuration_request.deserialize_aws_json_1_0(
                item
            )
        )
    return out
