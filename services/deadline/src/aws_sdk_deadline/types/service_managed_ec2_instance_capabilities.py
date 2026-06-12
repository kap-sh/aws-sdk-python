"""Generated from Smithy shape ``com.amazonaws.deadline#ServiceManagedEc2InstanceCapabilities``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.accelerator_capabilities
    import aws_sdk_deadline.types.cpu_architecture_type
    import aws_sdk_deadline.types.custom_fleet_amount_capabilities
    import aws_sdk_deadline.types.custom_fleet_attribute_capabilities
    import aws_sdk_deadline.types.ec2_ebs_volume
    import aws_sdk_deadline.types.instance_types
    import aws_sdk_deadline.types.memory_mi_b_range
    import aws_sdk_deadline.types.service_managed_fleet_operating_system_family
    import aws_sdk_deadline.types.v_cpu_count_range


class ServiceManagedEc2InstanceCapabilities(TypedDict):
    v_cpu_count: "aws_sdk_deadline.types.v_cpu_count_range.VCpuCountRange"
    """<p>The amount of vCPU to require for instances in this fleet.</p>"""
    memory_mi_b: "aws_sdk_deadline.types.memory_mi_b_range.MemoryMiBRange"
    """<p>The memory, as MiB, for the Amazon EC2 instance type.</p>"""
    os_family: "aws_sdk_deadline.types.service_managed_fleet_operating_system_family.ServiceManagedFleetOperatingSystemFamily"
    """<p>The operating system (OS) family.</p>"""
    cpu_architecture_type: (
        "aws_sdk_deadline.types.cpu_architecture_type.CpuArchitectureType"
    )
    """<p>The CPU architecture type.</p>"""
    root_ebs_volume: NotRequired["aws_sdk_deadline.types.ec2_ebs_volume.Ec2EbsVolume"]
    """<p>The root EBS volume.</p>"""
    accelerator_capabilities: NotRequired[
        "aws_sdk_deadline.types.accelerator_capabilities.AcceleratorCapabilities"
    ]
    """<p>Describes the GPU accelerator capabilities required for worker host instances in this fleet.</p>"""
    allowed_instance_types: NotRequired[
        "aws_sdk_deadline.types.instance_types.InstanceTypes"
    ]
    """<p>The allowable Amazon EC2 instance types.</p>"""
    excluded_instance_types: NotRequired[
        "aws_sdk_deadline.types.instance_types.InstanceTypes"
    ]
    """<p>The instance types to exclude from the fleet.</p>"""
    custom_amounts: NotRequired[
        "aws_sdk_deadline.types.custom_fleet_amount_capabilities.CustomFleetAmountCapabilities"
    ]
    """<p>The custom capability amounts to require for instances in this fleet.</p>"""
    custom_attributes: NotRequired[
        "aws_sdk_deadline.types.custom_fleet_attribute_capabilities.CustomFleetAttributeCapabilities"
    ]
    """<p>The custom capability attributes to require for instances in this fleet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceManagedEc2InstanceCapabilities) -> dict:
    out: dict = {}
    import aws_sdk_deadline.types.v_cpu_count_range

    out["vCpuCount"] = aws_sdk_deadline.types.v_cpu_count_range.serialize_json(
        value["v_cpu_count"]
    )
    import aws_sdk_deadline.types.memory_mi_b_range

    out["memoryMiB"] = aws_sdk_deadline.types.memory_mi_b_range.serialize_json(
        value["memory_mi_b"]
    )
    import aws_sdk_deadline.types.service_managed_fleet_operating_system_family

    out["osFamily"] = (
        aws_sdk_deadline.types.service_managed_fleet_operating_system_family.serialize_json(
            value["os_family"]
        )
    )
    import aws_sdk_deadline.types.cpu_architecture_type

    out["cpuArchitectureType"] = (
        aws_sdk_deadline.types.cpu_architecture_type.serialize_json(
            value["cpu_architecture_type"]
        )
    )
    if "root_ebs_volume" in value:
        import aws_sdk_deadline.types.ec2_ebs_volume

        out["rootEbsVolume"] = aws_sdk_deadline.types.ec2_ebs_volume.serialize_json(
            value["root_ebs_volume"]
        )
    if "accelerator_capabilities" in value:
        import aws_sdk_deadline.types.accelerator_capabilities

        out["acceleratorCapabilities"] = (
            aws_sdk_deadline.types.accelerator_capabilities.serialize_json(
                value["accelerator_capabilities"]
            )
        )
    if "allowed_instance_types" in value:
        import aws_sdk_deadline.types.instance_types

        out["allowedInstanceTypes"] = (
            aws_sdk_deadline.types.instance_types.serialize_json(
                value["allowed_instance_types"]
            )
        )
    if "excluded_instance_types" in value:
        import aws_sdk_deadline.types.instance_types

        out["excludedInstanceTypes"] = (
            aws_sdk_deadline.types.instance_types.serialize_json(
                value["excluded_instance_types"]
            )
        )
    if "custom_amounts" in value:
        import aws_sdk_deadline.types.custom_fleet_amount_capabilities

        out["customAmounts"] = (
            aws_sdk_deadline.types.custom_fleet_amount_capabilities.serialize_json(
                value["custom_amounts"]
            )
        )
    if "custom_attributes" in value:
        import aws_sdk_deadline.types.custom_fleet_attribute_capabilities

        out["customAttributes"] = (
            aws_sdk_deadline.types.custom_fleet_attribute_capabilities.serialize_json(
                value["custom_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceManagedEc2InstanceCapabilities:
    out: ServiceManagedEc2InstanceCapabilities = {}  # type: ignore[typeddict-item]
    if "vCpuCount" in data:
        import aws_sdk_deadline.types.v_cpu_count_range

        out["v_cpu_count"] = aws_sdk_deadline.types.v_cpu_count_range.deserialize_json(
            data["vCpuCount"]
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2InstanceCapabilities.v_cpu_count required"
        )
    if "memoryMiB" in data:
        import aws_sdk_deadline.types.memory_mi_b_range

        out["memory_mi_b"] = aws_sdk_deadline.types.memory_mi_b_range.deserialize_json(
            data["memoryMiB"]
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2InstanceCapabilities.memory_mi_b required"
        )
    if "osFamily" in data:
        import aws_sdk_deadline.types.service_managed_fleet_operating_system_family

        out["os_family"] = (
            aws_sdk_deadline.types.service_managed_fleet_operating_system_family.deserialize_json(
                data["osFamily"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2InstanceCapabilities.os_family required"
        )
    if "cpuArchitectureType" in data:
        import aws_sdk_deadline.types.cpu_architecture_type

        out["cpu_architecture_type"] = (
            aws_sdk_deadline.types.cpu_architecture_type.deserialize_json(
                data["cpuArchitectureType"]
            )
        )
    else:
        raise DeserializationError(
            "ServiceManagedEc2InstanceCapabilities.cpu_architecture_type required"
        )
    if "rootEbsVolume" in data:
        import aws_sdk_deadline.types.ec2_ebs_volume

        out["root_ebs_volume"] = aws_sdk_deadline.types.ec2_ebs_volume.deserialize_json(
            data["rootEbsVolume"]
        )
    if "acceleratorCapabilities" in data:
        import aws_sdk_deadline.types.accelerator_capabilities

        out["accelerator_capabilities"] = (
            aws_sdk_deadline.types.accelerator_capabilities.deserialize_json(
                data["acceleratorCapabilities"]
            )
        )
    if "allowedInstanceTypes" in data:
        import aws_sdk_deadline.types.instance_types

        out["allowed_instance_types"] = (
            aws_sdk_deadline.types.instance_types.deserialize_json(
                data["allowedInstanceTypes"]
            )
        )
    if "excludedInstanceTypes" in data:
        import aws_sdk_deadline.types.instance_types

        out["excluded_instance_types"] = (
            aws_sdk_deadline.types.instance_types.deserialize_json(
                data["excludedInstanceTypes"]
            )
        )
    if "customAmounts" in data:
        import aws_sdk_deadline.types.custom_fleet_amount_capabilities

        out["custom_amounts"] = (
            aws_sdk_deadline.types.custom_fleet_amount_capabilities.deserialize_json(
                data["customAmounts"]
            )
        )
    if "customAttributes" in data:
        import aws_sdk_deadline.types.custom_fleet_attribute_capabilities

        out["custom_attributes"] = (
            aws_sdk_deadline.types.custom_fleet_attribute_capabilities.deserialize_json(
                data["customAttributes"]
            )
        )
    return out
