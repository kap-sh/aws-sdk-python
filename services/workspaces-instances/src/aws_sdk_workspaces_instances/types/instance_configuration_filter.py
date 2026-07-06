"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#InstanceConfigurationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_instances.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.billing_mode
    import aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum
    import aws_sdk_workspaces_instances.types.platform_type_enum


class InstanceConfigurationFilter(TypedDict, closed=True):
    billing_mode: "aws_sdk_workspaces_instances.types.billing_mode.BillingMode"
    """<p>Filters WorkSpace Instance types based on supported billing modes. Allows customers to search for instance types that support their preferred billing model, such as HOURLY or MONTHLY billing.</p>"""
    platform_type: (
        "aws_sdk_workspaces_instances.types.platform_type_enum.PlatformTypeEnum"
    )
    """<p>Filters WorkSpace Instance types by operating system platform. Allows customers to find instances that support their desired OS, such as Windows, Linux/UNIX, Ubuntu Pro, RHEL, or SUSE.</p>"""
    tenancy: "aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum.InstanceConfigurationTenancyEnum"
    """<p>Filters WorkSpace Instance types by tenancy model. Allows customers to find instances that match their tenancy requirements, such as SHARED or DEDICATED.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InstanceConfigurationFilter) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_instances.types.billing_mode

    out["BillingMode"] = (
        aws_sdk_workspaces_instances.types.billing_mode.serialize_aws_json_1_0(
            value["billing_mode"]
        )
    )
    import aws_sdk_workspaces_instances.types.platform_type_enum

    out["PlatformType"] = (
        aws_sdk_workspaces_instances.types.platform_type_enum.serialize_aws_json_1_0(
            value["platform_type"]
        )
    )
    import aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum

    out["Tenancy"] = (
        aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum.serialize_aws_json_1_0(
            value["tenancy"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> InstanceConfigurationFilter:
    out: InstanceConfigurationFilter = {}  # type: ignore[typeddict-item]
    if "BillingMode" in data:
        import aws_sdk_workspaces_instances.types.billing_mode

        out["billing_mode"] = (
            aws_sdk_workspaces_instances.types.billing_mode.deserialize_aws_json_1_0(
                data["BillingMode"]
            )
        )
    else:
        raise DeserializationError("InstanceConfigurationFilter.billing_mode required")
    if "PlatformType" in data:
        import aws_sdk_workspaces_instances.types.platform_type_enum

        out["platform_type"] = (
            aws_sdk_workspaces_instances.types.platform_type_enum.deserialize_aws_json_1_0(
                data["PlatformType"]
            )
        )
    else:
        raise DeserializationError("InstanceConfigurationFilter.platform_type required")
    if "Tenancy" in data:
        import aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum

        out["tenancy"] = (
            aws_sdk_workspaces_instances.types.instance_configuration_tenancy_enum.deserialize_aws_json_1_0(
                data["Tenancy"]
            )
        )
    else:
        raise DeserializationError("InstanceConfigurationFilter.tenancy required")
    return out
