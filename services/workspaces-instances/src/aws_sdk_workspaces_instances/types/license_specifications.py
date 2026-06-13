"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#LicenseSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.license_configuration_request

LicenseSpecifications: TypeAlias = list[
    "aws_sdk_workspaces_instances.types.license_configuration_request.LicenseConfigurationRequest"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseSpecifications) -> list:
    import aws_sdk_workspaces_instances.types.license_configuration_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces_instances.types.license_configuration_request.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseSpecifications:
    import aws_sdk_workspaces_instances.types.license_configuration_request

    out: LicenseSpecifications = []
    for item in data:
        out.append(
            aws_sdk_workspaces_instances.types.license_configuration_request.deserialize_aws_json_1_0(
                item
            )
        )
    return out
