"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ManagedInstanceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.block_device_mappings
    import aws_sdk_workspaces_instances.types.capacity_reservation_specification
    import aws_sdk_workspaces_instances.types.cpu_options_request
    import aws_sdk_workspaces_instances.types.credit_specification_request
    import aws_sdk_workspaces_instances.types.enclave_options_request
    import aws_sdk_workspaces_instances.types.hibernation_options_request
    import aws_sdk_workspaces_instances.types.iam_instance_profile_specification
    import aws_sdk_workspaces_instances.types.image_id
    import aws_sdk_workspaces_instances.types.instance_maintenance_options_request
    import aws_sdk_workspaces_instances.types.instance_market_options_request
    import aws_sdk_workspaces_instances.types.instance_metadata_options_request
    import aws_sdk_workspaces_instances.types.instance_network_performance_options_request
    import aws_sdk_workspaces_instances.types.instance_type
    import aws_sdk_workspaces_instances.types.ipv4_address
    import aws_sdk_workspaces_instances.types.ipv6_addresses
    import aws_sdk_workspaces_instances.types.license_specifications
    import aws_sdk_workspaces_instances.types.network_interfaces
    import aws_sdk_workspaces_instances.types.non_negative_integer
    import aws_sdk_workspaces_instances.types.placement
    import aws_sdk_workspaces_instances.types.private_dns_name_options_request
    import aws_sdk_workspaces_instances.types.run_instances_monitoring_enabled
    import aws_sdk_workspaces_instances.types.security_group_ids
    import aws_sdk_workspaces_instances.types.security_group_names
    import aws_sdk_workspaces_instances.types.string128
    import aws_sdk_workspaces_instances.types.string64
    import aws_sdk_workspaces_instances.types.subnet_id
    import aws_sdk_workspaces_instances.types.tag_specifications
    import aws_sdk_workspaces_instances.types.user_data

class ManagedInstanceRequest(TypedDict):
    block_device_mappings: NotRequired["aws_sdk_workspaces_instances.types.block_device_mappings.BlockDeviceMappings"]
    """<p>Configures block device mappings for storage.</p>"""
    capacity_reservation_specification: NotRequired["aws_sdk_workspaces_instances.types.capacity_reservation_specification.CapacityReservationSpecification"]
    """<p>Specifies capacity reservation preferences.</p>"""
    cpu_options: NotRequired["aws_sdk_workspaces_instances.types.cpu_options_request.CpuOptionsRequest"]
    """<p>Configures CPU-specific settings.</p>"""
    credit_specification: NotRequired["aws_sdk_workspaces_instances.types.credit_specification_request.CreditSpecificationRequest"]
    """<p>Defines CPU credit configuration for burstable instances.</p>"""
    disable_api_stop: NotRequired["bool"]
    """<p>Prevents API-initiated instance stop.</p>"""
    ebs_optimized: NotRequired["bool"]
    """<p>Enables optimized EBS performance.</p>"""
    enable_primary_ipv6: NotRequired["bool"]
    """<p>Enables primary IPv6 address configuration.</p>"""
    enclave_options: NotRequired["aws_sdk_workspaces_instances.types.enclave_options_request.EnclaveOptionsRequest"]
    """<p>Configures AWS Nitro Enclave settings.</p>"""
    hibernation_options: NotRequired["aws_sdk_workspaces_instances.types.hibernation_options_request.HibernationOptionsRequest"]
    """<p>Configures instance hibernation capabilities.</p>"""
    iam_instance_profile: NotRequired["aws_sdk_workspaces_instances.types.iam_instance_profile_specification.IamInstanceProfileSpecification"]
    """<p>Specifies IAM instance profile configuration.</p>"""
    image_id: NotRequired["aws_sdk_workspaces_instances.types.image_id.ImageId"]
    """<p>Identifies the Amazon Machine Image (AMI) for the instance.</p>"""
    instance_market_options: NotRequired["aws_sdk_workspaces_instances.types.instance_market_options_request.InstanceMarketOptionsRequest"]
    """<p>Configures marketplace-specific deployment options.</p>"""
    instance_type: NotRequired["aws_sdk_workspaces_instances.types.instance_type.InstanceType"]
    """<p>Specifies the WorkSpace Instance type.</p>"""
    ipv6_addresses: NotRequired["aws_sdk_workspaces_instances.types.ipv6_addresses.Ipv6Addresses"]
    """<p>Configures specific IPv6 addresses.</p>"""
    ipv6_address_count: NotRequired["aws_sdk_workspaces_instances.types.non_negative_integer.NonNegativeInteger"]
    """<p>Specifies number of IPv6 addresses to assign.</p>"""
    kernel_id: NotRequired["aws_sdk_workspaces_instances.types.string128.String128"]
    """<p>Identifies the kernel for the instance.</p>"""
    key_name: NotRequired["aws_sdk_workspaces_instances.types.string64.String64"]
    """<p>Specifies the key pair for instance access.</p>"""
    license_specifications: NotRequired["aws_sdk_workspaces_instances.types.license_specifications.LicenseSpecifications"]
    """<p>Configures license-related settings.</p>"""
    maintenance_options: NotRequired["aws_sdk_workspaces_instances.types.instance_maintenance_options_request.InstanceMaintenanceOptionsRequest"]
    """<p>Defines automatic maintenance settings.</p>"""
    metadata_options: NotRequired["aws_sdk_workspaces_instances.types.instance_metadata_options_request.InstanceMetadataOptionsRequest"]
    """<p>Configures instance metadata service settings.</p>"""
    monitoring: NotRequired["aws_sdk_workspaces_instances.types.run_instances_monitoring_enabled.RunInstancesMonitoringEnabled"]
    """<p>Enables or disables detailed instance monitoring.</p>"""
    network_interfaces: NotRequired["aws_sdk_workspaces_instances.types.network_interfaces.NetworkInterfaces"]
    """<p>Configures network interface settings.</p>"""
    network_performance_options: NotRequired["aws_sdk_workspaces_instances.types.instance_network_performance_options_request.InstanceNetworkPerformanceOptionsRequest"]
    """<p>Defines network performance configuration.</p>"""
    placement: NotRequired["aws_sdk_workspaces_instances.types.placement.Placement"]
    """<p>Specifies instance placement preferences.</p>"""
    private_dns_name_options: NotRequired["aws_sdk_workspaces_instances.types.private_dns_name_options_request.PrivateDnsNameOptionsRequest"]
    """<p>Configures private DNS name settings.</p>"""
    private_ip_address: NotRequired["aws_sdk_workspaces_instances.types.ipv4_address.Ipv4Address"]
    """<p>Specifies the primary private IP address.</p>"""
    ramdisk_id: NotRequired["aws_sdk_workspaces_instances.types.string128.String128"]
    """<p>Identifies the ramdisk for the instance.</p>"""
    security_group_ids: NotRequired["aws_sdk_workspaces_instances.types.security_group_ids.SecurityGroupIds"]
    """<p>Specifies security group identifiers.</p>"""
    security_groups: NotRequired["aws_sdk_workspaces_instances.types.security_group_names.SecurityGroupNames"]
    """<p>Configures security group settings.</p>"""
    subnet_id: NotRequired["aws_sdk_workspaces_instances.types.subnet_id.SubnetId"]
    """<p>Identifies the subnet for the instance.</p>"""
    tag_specifications: NotRequired["aws_sdk_workspaces_instances.types.tag_specifications.TagSpecifications"]
    """<p>Configures resource tagging specifications.</p>"""
    user_data: NotRequired["aws_sdk_workspaces_instances.types.user_data.UserData"]
    """<p>Provides custom initialization data for the instance.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedInstanceRequest) -> dict:
    out: dict = {}
    if "block_device_mappings" in value:
        import aws_sdk_workspaces_instances.types.block_device_mappings
        out["BlockDeviceMappings"] = aws_sdk_workspaces_instances.types.block_device_mappings.serialize_aws_json_1_0(value["block_device_mappings"])
    if "capacity_reservation_specification" in value:
        import aws_sdk_workspaces_instances.types.capacity_reservation_specification
        out["CapacityReservationSpecification"] = aws_sdk_workspaces_instances.types.capacity_reservation_specification.serialize_aws_json_1_0(value["capacity_reservation_specification"])
    if "cpu_options" in value:
        import aws_sdk_workspaces_instances.types.cpu_options_request
        out["CpuOptions"] = aws_sdk_workspaces_instances.types.cpu_options_request.serialize_aws_json_1_0(value["cpu_options"])
    if "credit_specification" in value:
        import aws_sdk_workspaces_instances.types.credit_specification_request
        out["CreditSpecification"] = aws_sdk_workspaces_instances.types.credit_specification_request.serialize_aws_json_1_0(value["credit_specification"])
    if "disable_api_stop" in value:
        out["DisableApiStop"] = value["disable_api_stop"]
    if "ebs_optimized" in value:
        out["EbsOptimized"] = value["ebs_optimized"]
    if "enable_primary_ipv6" in value:
        out["EnablePrimaryIpv6"] = value["enable_primary_ipv6"]
    if "enclave_options" in value:
        import aws_sdk_workspaces_instances.types.enclave_options_request
        out["EnclaveOptions"] = aws_sdk_workspaces_instances.types.enclave_options_request.serialize_aws_json_1_0(value["enclave_options"])
    if "hibernation_options" in value:
        import aws_sdk_workspaces_instances.types.hibernation_options_request
        out["HibernationOptions"] = aws_sdk_workspaces_instances.types.hibernation_options_request.serialize_aws_json_1_0(value["hibernation_options"])
    if "iam_instance_profile" in value:
        import aws_sdk_workspaces_instances.types.iam_instance_profile_specification
        out["IamInstanceProfile"] = aws_sdk_workspaces_instances.types.iam_instance_profile_specification.serialize_aws_json_1_0(value["iam_instance_profile"])
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "instance_market_options" in value:
        import aws_sdk_workspaces_instances.types.instance_market_options_request
        out["InstanceMarketOptions"] = aws_sdk_workspaces_instances.types.instance_market_options_request.serialize_aws_json_1_0(value["instance_market_options"])
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "ipv6_addresses" in value:
        import aws_sdk_workspaces_instances.types.ipv6_addresses
        out["Ipv6Addresses"] = aws_sdk_workspaces_instances.types.ipv6_addresses.serialize_aws_json_1_0(value["ipv6_addresses"])
    if "ipv6_address_count" in value:
        out["Ipv6AddressCount"] = value["ipv6_address_count"]
    if "kernel_id" in value:
        out["KernelId"] = value["kernel_id"]
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "license_specifications" in value:
        import aws_sdk_workspaces_instances.types.license_specifications
        out["LicenseSpecifications"] = aws_sdk_workspaces_instances.types.license_specifications.serialize_aws_json_1_0(value["license_specifications"])
    if "maintenance_options" in value:
        import aws_sdk_workspaces_instances.types.instance_maintenance_options_request
        out["MaintenanceOptions"] = aws_sdk_workspaces_instances.types.instance_maintenance_options_request.serialize_aws_json_1_0(value["maintenance_options"])
    if "metadata_options" in value:
        import aws_sdk_workspaces_instances.types.instance_metadata_options_request
        out["MetadataOptions"] = aws_sdk_workspaces_instances.types.instance_metadata_options_request.serialize_aws_json_1_0(value["metadata_options"])
    if "monitoring" in value:
        import aws_sdk_workspaces_instances.types.run_instances_monitoring_enabled
        out["Monitoring"] = aws_sdk_workspaces_instances.types.run_instances_monitoring_enabled.serialize_aws_json_1_0(value["monitoring"])
    if "network_interfaces" in value:
        import aws_sdk_workspaces_instances.types.network_interfaces
        out["NetworkInterfaces"] = aws_sdk_workspaces_instances.types.network_interfaces.serialize_aws_json_1_0(value["network_interfaces"])
    if "network_performance_options" in value:
        import aws_sdk_workspaces_instances.types.instance_network_performance_options_request
        out["NetworkPerformanceOptions"] = aws_sdk_workspaces_instances.types.instance_network_performance_options_request.serialize_aws_json_1_0(value["network_performance_options"])
    if "placement" in value:
        import aws_sdk_workspaces_instances.types.placement
        out["Placement"] = aws_sdk_workspaces_instances.types.placement.serialize_aws_json_1_0(value["placement"])
    if "private_dns_name_options" in value:
        import aws_sdk_workspaces_instances.types.private_dns_name_options_request
        out["PrivateDnsNameOptions"] = aws_sdk_workspaces_instances.types.private_dns_name_options_request.serialize_aws_json_1_0(value["private_dns_name_options"])
    if "private_ip_address" in value:
        out["PrivateIpAddress"] = value["private_ip_address"]
    if "ramdisk_id" in value:
        out["RamdiskId"] = value["ramdisk_id"]
    if "security_group_ids" in value:
        import aws_sdk_workspaces_instances.types.security_group_ids
        out["SecurityGroupIds"] = aws_sdk_workspaces_instances.types.security_group_ids.serialize_aws_json_1_0(value["security_group_ids"])
    if "security_groups" in value:
        import aws_sdk_workspaces_instances.types.security_group_names
        out["SecurityGroups"] = aws_sdk_workspaces_instances.types.security_group_names.serialize_aws_json_1_0(value["security_groups"])
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "tag_specifications" in value:
        import aws_sdk_workspaces_instances.types.tag_specifications
        out["TagSpecifications"] = aws_sdk_workspaces_instances.types.tag_specifications.serialize_aws_json_1_0(value["tag_specifications"])
    if "user_data" in value:
        out["UserData"] = value["user_data"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ManagedInstanceRequest:
    out: ManagedInstanceRequest = {}  # type: ignore[typeddict-item]
    if "BlockDeviceMappings" in data:
        import aws_sdk_workspaces_instances.types.block_device_mappings
        out["block_device_mappings"] = aws_sdk_workspaces_instances.types.block_device_mappings.deserialize_aws_json_1_0(data["BlockDeviceMappings"])
    if "CapacityReservationSpecification" in data:
        import aws_sdk_workspaces_instances.types.capacity_reservation_specification
        out["capacity_reservation_specification"] = aws_sdk_workspaces_instances.types.capacity_reservation_specification.deserialize_aws_json_1_0(data["CapacityReservationSpecification"])
    if "CpuOptions" in data:
        import aws_sdk_workspaces_instances.types.cpu_options_request
        out["cpu_options"] = aws_sdk_workspaces_instances.types.cpu_options_request.deserialize_aws_json_1_0(data["CpuOptions"])
    if "CreditSpecification" in data:
        import aws_sdk_workspaces_instances.types.credit_specification_request
        out["credit_specification"] = aws_sdk_workspaces_instances.types.credit_specification_request.deserialize_aws_json_1_0(data["CreditSpecification"])
    if "DisableApiStop" in data:
        out["disable_api_stop"] = data["DisableApiStop"]
    if "EbsOptimized" in data:
        out["ebs_optimized"] = data["EbsOptimized"]
    if "EnablePrimaryIpv6" in data:
        out["enable_primary_ipv6"] = data["EnablePrimaryIpv6"]
    if "EnclaveOptions" in data:
        import aws_sdk_workspaces_instances.types.enclave_options_request
        out["enclave_options"] = aws_sdk_workspaces_instances.types.enclave_options_request.deserialize_aws_json_1_0(data["EnclaveOptions"])
    if "HibernationOptions" in data:
        import aws_sdk_workspaces_instances.types.hibernation_options_request
        out["hibernation_options"] = aws_sdk_workspaces_instances.types.hibernation_options_request.deserialize_aws_json_1_0(data["HibernationOptions"])
    if "IamInstanceProfile" in data:
        import aws_sdk_workspaces_instances.types.iam_instance_profile_specification
        out["iam_instance_profile"] = aws_sdk_workspaces_instances.types.iam_instance_profile_specification.deserialize_aws_json_1_0(data["IamInstanceProfile"])
    if "ImageId" in data:
        out["image_id"] = data["ImageId"]
    if "InstanceMarketOptions" in data:
        import aws_sdk_workspaces_instances.types.instance_market_options_request
        out["instance_market_options"] = aws_sdk_workspaces_instances.types.instance_market_options_request.deserialize_aws_json_1_0(data["InstanceMarketOptions"])
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "Ipv6Addresses" in data:
        import aws_sdk_workspaces_instances.types.ipv6_addresses
        out["ipv6_addresses"] = aws_sdk_workspaces_instances.types.ipv6_addresses.deserialize_aws_json_1_0(data["Ipv6Addresses"])
    if "Ipv6AddressCount" in data:
        out["ipv6_address_count"] = data["Ipv6AddressCount"]
    if "KernelId" in data:
        out["kernel_id"] = data["KernelId"]
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    if "LicenseSpecifications" in data:
        import aws_sdk_workspaces_instances.types.license_specifications
        out["license_specifications"] = aws_sdk_workspaces_instances.types.license_specifications.deserialize_aws_json_1_0(data["LicenseSpecifications"])
    if "MaintenanceOptions" in data:
        import aws_sdk_workspaces_instances.types.instance_maintenance_options_request
        out["maintenance_options"] = aws_sdk_workspaces_instances.types.instance_maintenance_options_request.deserialize_aws_json_1_0(data["MaintenanceOptions"])
    if "MetadataOptions" in data:
        import aws_sdk_workspaces_instances.types.instance_metadata_options_request
        out["metadata_options"] = aws_sdk_workspaces_instances.types.instance_metadata_options_request.deserialize_aws_json_1_0(data["MetadataOptions"])
    if "Monitoring" in data:
        import aws_sdk_workspaces_instances.types.run_instances_monitoring_enabled
        out["monitoring"] = aws_sdk_workspaces_instances.types.run_instances_monitoring_enabled.deserialize_aws_json_1_0(data["Monitoring"])
    if "NetworkInterfaces" in data:
        import aws_sdk_workspaces_instances.types.network_interfaces
        out["network_interfaces"] = aws_sdk_workspaces_instances.types.network_interfaces.deserialize_aws_json_1_0(data["NetworkInterfaces"])
    if "NetworkPerformanceOptions" in data:
        import aws_sdk_workspaces_instances.types.instance_network_performance_options_request
        out["network_performance_options"] = aws_sdk_workspaces_instances.types.instance_network_performance_options_request.deserialize_aws_json_1_0(data["NetworkPerformanceOptions"])
    if "Placement" in data:
        import aws_sdk_workspaces_instances.types.placement
        out["placement"] = aws_sdk_workspaces_instances.types.placement.deserialize_aws_json_1_0(data["Placement"])
    if "PrivateDnsNameOptions" in data:
        import aws_sdk_workspaces_instances.types.private_dns_name_options_request
        out["private_dns_name_options"] = aws_sdk_workspaces_instances.types.private_dns_name_options_request.deserialize_aws_json_1_0(data["PrivateDnsNameOptions"])
    if "PrivateIpAddress" in data:
        out["private_ip_address"] = data["PrivateIpAddress"]
    if "RamdiskId" in data:
        out["ramdisk_id"] = data["RamdiskId"]
    if "SecurityGroupIds" in data:
        import aws_sdk_workspaces_instances.types.security_group_ids
        out["security_group_ids"] = aws_sdk_workspaces_instances.types.security_group_ids.deserialize_aws_json_1_0(data["SecurityGroupIds"])
    if "SecurityGroups" in data:
        import aws_sdk_workspaces_instances.types.security_group_names
        out["security_groups"] = aws_sdk_workspaces_instances.types.security_group_names.deserialize_aws_json_1_0(data["SecurityGroups"])
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "TagSpecifications" in data:
        import aws_sdk_workspaces_instances.types.tag_specifications
        out["tag_specifications"] = aws_sdk_workspaces_instances.types.tag_specifications.deserialize_aws_json_1_0(data["TagSpecifications"])
    if "UserData" in data:
        out["user_data"] = data["UserData"]
    return out