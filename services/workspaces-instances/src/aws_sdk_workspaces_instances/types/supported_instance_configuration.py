"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#SupportedInstanceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.billing_mode
    import aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum
    import aws_sdk_workspaces_instances.types.platform_type_enum


class SupportedInstanceConfiguration(TypedDict):
    billing_mode: NotRequired[
        "aws_sdk_workspaces_instances.types.billing_mode.BillingMode"
    ]
    """<p>Specifies the billing mode supported in this configuration combination.</p>"""
    platform_type: NotRequired[
        "aws_sdk_workspaces_instances.types.platform_type_enum.PlatformTypeEnum"
    ]
    """<p>Specifies the operating system platform supported in this configuration combination.</p>"""
    tenancy: NotRequired[
        "aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum.InstanceConfigurationTenancyEnum"
    ]
    """<p>Specifies the tenancy model supported in this configuration combination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupportedInstanceConfiguration) -> dict:
    out: dict = {}
    if "billing_mode" in value:
        import aws_sdk_workspaces_instances.types.billing_mode

        out["BillingMode"] = (
            aws_sdk_workspaces_instances.types.billing_mode.serialize_aws_json_1_0(
                value["billing_mode"]
            )
        )
    if "platform_type" in value:
        import aws_sdk_workspaces_instances.types.platform_type_enum

        out["PlatformType"] = (
            aws_sdk_workspaces_instances.types.platform_type_enum.serialize_aws_json_1_0(
                value["platform_type"]
            )
        )
    if "tenancy" in value:
        import aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum

        out["Tenancy"] = (
            aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum.serialize_aws_json_1_0(
                value["tenancy"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SupportedInstanceConfiguration:
    out: SupportedInstanceConfiguration = {}  # type: ignore[typeddict-item]
    if "BillingMode" in data:
        import aws_sdk_workspaces_instances.types.billing_mode

        out["billing_mode"] = (
            aws_sdk_workspaces_instances.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    if "PlatformType" in data:
        import aws_sdk_workspaces_instances.types.platform_type_enum

        out["platform_type"] = (
            aws_sdk_workspaces_instances.types.platform_type_enum.deserialize_aws_json_1_0(
                data["PlatformType"]
            )
        )
    if "Tenancy" in data:
        import aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum

        out["tenancy"] = (
            aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum.deserialize_aws_json_1_0(
                data["Tenancy"]
            )
        )
    return out
