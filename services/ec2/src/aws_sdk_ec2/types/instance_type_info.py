"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.auto_recovery_flag
    import aws_sdk_ec2.types.bare_metal_flag
    import aws_sdk_ec2.types.boot_mode_type_list
    import aws_sdk_ec2.types.burstable_performance_flag
    import aws_sdk_ec2.types.current_generation_flag
    import aws_sdk_ec2.types.dedicated_host_flag
    import aws_sdk_ec2.types.ebs_info
    import aws_sdk_ec2.types.fpga_info
    import aws_sdk_ec2.types.free_tier_eligible_flag
    import aws_sdk_ec2.types.gpu_info
    import aws_sdk_ec2.types.hibernation_flag
    import aws_sdk_ec2.types.inference_accelerator_info
    import aws_sdk_ec2.types.instance_storage_flag
    import aws_sdk_ec2.types.instance_storage_info
    import aws_sdk_ec2.types.instance_type
    import aws_sdk_ec2.types.instance_type_hypervisor
    import aws_sdk_ec2.types.media_accelerator_info
    import aws_sdk_ec2.types.memory_info
    import aws_sdk_ec2.types.network_info
    import aws_sdk_ec2.types.neuron_info
    import aws_sdk_ec2.types.nitro_enclaves_support
    import aws_sdk_ec2.types.nitro_tpm_info
    import aws_sdk_ec2.types.nitro_tpm_support
    import aws_sdk_ec2.types.phc_support
    import aws_sdk_ec2.types.placement_group_info
    import aws_sdk_ec2.types.processor_info
    import aws_sdk_ec2.types.reboot_migration_support
    import aws_sdk_ec2.types.root_device_type_list
    import aws_sdk_ec2.types.supported_in_region
    import aws_sdk_ec2.types.usage_class_type_list
    import aws_sdk_ec2.types.v_cpu_info
    import aws_sdk_ec2.types.virtualization_type_list


class InstanceTypeInfo(TypedDict):
    instance_type: NotRequired["aws_sdk_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html\">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    current_generation: NotRequired[
        "aws_sdk_ec2.types.current_generation_flag.CurrentGenerationFlag"
    ]
    """<p>Indicates whether the instance type is current generation.</p>"""
    free_tier_eligible: NotRequired[
        "aws_sdk_ec2.types.free_tier_eligible_flag.FreeTierEligibleFlag"
    ]
    """<p>Indicates whether the instance type is eligible for the free tier.</p>"""
    supported_usage_classes: NotRequired[
        "aws_sdk_ec2.types.usage_class_type_list.UsageClassTypeList"
    ]
    """<p>Indicates whether the instance type is offered for spot, On-Demand, or Capacity Blocks.</p>"""
    supported_root_device_types: NotRequired[
        "aws_sdk_ec2.types.root_device_type_list.RootDeviceTypeList"
    ]
    """<p>The supported root device types.</p>"""
    supported_virtualization_types: NotRequired[
        "aws_sdk_ec2.types.virtualization_type_list.VirtualizationTypeList"
    ]
    """<p>The supported virtualization types.</p>"""
    bare_metal: NotRequired["aws_sdk_ec2.types.bare_metal_flag.BareMetalFlag"]
    """<p>Indicates whether the instance is a bare metal instance type.</p>"""
    hypervisor: NotRequired[
        "aws_sdk_ec2.types.instance_type_hypervisor.InstanceTypeHypervisor"
    ]
    """<p>The hypervisor for the instance type.</p>"""
    processor_info: NotRequired["aws_sdk_ec2.types.processor_info.ProcessorInfo"]
    """<p>Describes the processor.</p>"""
    v_cpu_info: NotRequired["aws_sdk_ec2.types.v_cpu_info.VCpuInfo"]
    """<p>Describes the vCPU configurations for the instance type.</p>"""
    memory_info: NotRequired["aws_sdk_ec2.types.memory_info.MemoryInfo"]
    """<p>Describes the memory for the instance type.</p>"""
    instance_storage_supported: NotRequired[
        "aws_sdk_ec2.types.instance_storage_flag.InstanceStorageFlag"
    ]
    """<p>Indicates whether instance storage is supported.</p>"""
    instance_storage_info: NotRequired[
        "aws_sdk_ec2.types.instance_storage_info.InstanceStorageInfo"
    ]
    """<p>Describes the instance storage for the instance type.</p>"""
    ebs_info: NotRequired["aws_sdk_ec2.types.ebs_info.EbsInfo"]
    """<p>Describes the Amazon EBS settings for the instance type.</p>"""
    network_info: NotRequired["aws_sdk_ec2.types.network_info.NetworkInfo"]
    """<p>Describes the network settings for the instance type.</p>"""
    gpu_info: NotRequired["aws_sdk_ec2.types.gpu_info.GpuInfo"]
    """<p>Describes the GPU accelerator settings for the instance type.</p>"""
    fpga_info: NotRequired["aws_sdk_ec2.types.fpga_info.FpgaInfo"]
    """<p>Describes the FPGA accelerator settings for the instance type.</p>"""
    placement_group_info: NotRequired[
        "aws_sdk_ec2.types.placement_group_info.PlacementGroupInfo"
    ]
    """<p>Describes the placement group settings for the instance type.</p>"""
    inference_accelerator_info: NotRequired[
        "aws_sdk_ec2.types.inference_accelerator_info.InferenceAcceleratorInfo"
    ]
    """<p>Describes the Inference accelerator settings for the instance type.</p>"""
    hibernation_supported: NotRequired[
        "aws_sdk_ec2.types.hibernation_flag.HibernationFlag"
    ]
    """<p>Indicates whether On-Demand hibernation is supported.</p>"""
    burstable_performance_supported: NotRequired[
        "aws_sdk_ec2.types.burstable_performance_flag.BurstablePerformanceFlag"
    ]
    """<p>Indicates whether the instance type is a burstable performance T instance type. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html\">Burstable performance instances</a>.</p>"""
    dedicated_hosts_supported: NotRequired[
        "aws_sdk_ec2.types.dedicated_host_flag.DedicatedHostFlag"
    ]
    """<p>Indicates whether Dedicated Hosts are supported on the instance type.</p>"""
    auto_recovery_supported: NotRequired[
        "aws_sdk_ec2.types.auto_recovery_flag.AutoRecoveryFlag"
    ]
    """<p>Indicates whether Amazon CloudWatch action based recovery is supported.</p>"""
    supported_boot_modes: NotRequired[
        "aws_sdk_ec2.types.boot_mode_type_list.BootModeTypeList"
    ]
    """<p>The supported boot modes. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html\">Boot modes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    nitro_enclaves_support: NotRequired[
        "aws_sdk_ec2.types.nitro_enclaves_support.NitroEnclavesSupport"
    ]
    """<p>Indicates whether Nitro Enclaves is supported.</p>"""
    nitro_tpm_support: NotRequired[
        "aws_sdk_ec2.types.nitro_tpm_support.NitroTpmSupport"
    ]
    """<p>Indicates whether NitroTPM is supported.</p>"""
    nitro_tpm_info: NotRequired["aws_sdk_ec2.types.nitro_tpm_info.NitroTpmInfo"]
    """<p>Describes the supported NitroTPM versions for the instance type.</p>"""
    media_accelerator_info: NotRequired[
        "aws_sdk_ec2.types.media_accelerator_info.MediaAcceleratorInfo"
    ]
    """<p>Describes the media accelerator settings for the instance type.</p>"""
    neuron_info: NotRequired["aws_sdk_ec2.types.neuron_info.NeuronInfo"]
    """<p>Describes the Neuron accelerator settings for the instance type.</p>"""
    phc_support: NotRequired["aws_sdk_ec2.types.phc_support.PhcSupport"]
    """<p>Indicates whether a local Precision Time Protocol (PTP) hardware clock (PHC) is supported.</p>"""
    reboot_migration_support: NotRequired[
        "aws_sdk_ec2.types.reboot_migration_support.RebootMigrationSupport"
    ]
    """<p>Indicates whether reboot migration during a user-initiated reboot is supported for instances that have a scheduled <code>system-reboot</code> event. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/schedevents_actions_reboot.html#reboot-migration\">Enable or disable reboot migration</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    supported_in_region: NotRequired[
        "aws_sdk_ec2.types.supported_in_region.SupportedInRegion"
    ]
    """<p>Indicates whether the instance type is supported in the current Region.</p>"""
