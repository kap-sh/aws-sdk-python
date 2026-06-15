"""Generated from Smithy shape ``com.amazonaws.batch#ComputeResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.compute_scaling_policy
    import aws_sdk_batch.types.cr_allocation_strategy
    import aws_sdk_batch.types.cr_type
    import aws_sdk_batch.types.ec2_configuration_list
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.launch_template_specification
    import aws_sdk_batch.types.string
    import aws_sdk_batch.types.string_list
    import aws_sdk_batch.types.tags_map


class ComputeResource(TypedDict):
    type: NotRequired["aws_sdk_batch.types.cr_type.CRType"]
    r"""<p>The type of compute environment: <code>EC2</code>, <code>SPOT</code>, <code>FARGATE</code>, or <code>FARGATE_SPOT</code>. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/compute_environments.html\">Compute environments</a> in the <i>Batch User Guide</i>.</p> <p> If you choose <code>SPOT</code>, you must also specify an Amazon EC2 Spot Fleet role with the <code>spotIamFleetRole</code> parameter. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html\">Amazon EC2 spot fleet role</a> in the <i>Batch User Guide</i>.</p> <note> <p>Multi-node parallel jobs aren't supported on Spot Instances.</p> </note>"""
    allocation_strategy: NotRequired[
        "aws_sdk_batch.types.cr_allocation_strategy.CRAllocationStrategy"
    ]
    r"""<p>The allocation strategy to use for the compute resource if not enough instances of the best fitting instance type can be allocated. This might be because of availability of the instance type in the Region or <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html\">Amazon EC2 service limits</a>. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/allocation-strategies.html\">Allocation strategies</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note> <note> <p>This parameter is required for Amazon EKS compute environments. For Amazon ECS compute environments, if this parameter isn't specified, the <code>BEST_FIT</code> allocation strategy is used by default.</p> </note> <dl> <dt>BEST_FIT (default)</dt> <dd> <p>Batch selects an instance type that best fits the needs of the jobs with a preference for the lowest-cost instance type. If additional instances of the selected instance type aren't available, Batch waits for the additional instances to be available. If there aren't enough instances available or the user is reaching <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html\">Amazon EC2 service limits</a>, additional jobs aren't run until the currently running jobs are completed. This allocation strategy keeps costs lower but can limit scaling. If you're using Spot Fleets with <code>BEST_FIT</code>, the Spot Fleet IAM Role must be specified. Compute resources that use a <code>BEST_FIT</code> allocation strategy don't support infrastructure updates and can't update some parameters. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html\">Updating compute environments</a> in the <i>Batch User Guide</i>.</p> </dd> <dt>BEST_FIT_PROGRESSIVE</dt> <dd> <p>Batch selects additional instance types that are large enough to meet the requirements of the jobs in the queue. Its preference is for instance types with lower cost vCPUs. If additional instances of the previously selected instance types aren't available, Batch selects new instance types.</p> </dd> <dt>SPOT_CAPACITY_OPTIMIZED</dt> <dd> <p>Batch selects one or more instance types that are large enough to meet the requirements of the jobs in the queue. Its preference is for instance types that are less likely to be interrupted. This allocation strategy is only available for Spot Instance compute resources.</p> </dd> <dt>SPOT_PRICE_CAPACITY_OPTIMIZED</dt> <dd> <p>The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price. This allocation strategy is only available for Spot Instance compute resources.</p> </dd> </dl> <p>With <code>BEST_FIT_PROGRESSIVE</code>,<code>SPOT_CAPACITY_OPTIMIZED</code> and <code>SPOT_PRICE_CAPACITY_OPTIMIZED</code> (recommended) strategies using On-Demand or Spot Instances, and the <code>BEST_FIT</code> strategy using Spot Instances, Batch might need to exceed <code>maxvCpus</code> to meet your capacity requirements. In this event, Batch never exceeds <code>maxvCpus</code> by more than a single instance.</p>"""
    minv_cpus: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The minimum number of vCPUs that a compute environment should maintain (even if the compute environment is <code>DISABLED</code>).</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    maxv_cpus: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The maximum number of vCPUs that a compute environment can support.</p> <note> <p>With <code>BEST_FIT_PROGRESSIVE</code>,<code>SPOT_CAPACITY_OPTIMIZED</code> and <code>SPOT_PRICE_CAPACITY_OPTIMIZED</code> (recommended) strategies using On-Demand or Spot Instances, and the <code>BEST_FIT</code> strategy using Spot Instances, Batch might need to exceed <code>maxvCpus</code> to meet your capacity requirements. In this event, Batch never exceeds <code>maxvCpus</code> by more than a single instance.</p> </note>"""
    desiredv_cpus: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The desired number of vCPUS in the compute environment. Batch modifies this value between the minimum and maximum values based on job queue demand.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    instance_types: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    r"""<p>The instances types that can be launched. You can specify instance families to launch any instance type within those families (for example, <code>c5</code> or <code>p3</code>), or you can specify specific sizes within a family (such as <code>c5.8xlarge</code>).</p> <p>Batch can select the instance type for you if you choose one of the following:</p> <ul> <li> <p> <code>default_x86_64</code> to choose x86 based instance types (from the <code>m6i</code>, <code>c6i</code>, <code>r6i</code>, and <code>c7i</code> instance families) that matches the resource demands of the job queue.</p> </li> <li> <p> <code>default_arm64</code> to choose ARM based instance types (from the <code>m6g</code>, <code>c6g</code>, <code>r6g</code>, and <code>c7g</code> instance families) that matches the resource demands of the job queue.</p> </li> <li> <p> <code>optimal</code> Semantically equivalent to <code>default_x86_64</code>, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/optimal-default-instance-troubleshooting.html\">Optimal instance type configuration to receive automatic instance family updates</a> for details.</p> </li> </ul> <note> <p>Instance family availability varies by Amazon Web Services Region. For example, some Amazon Web Services Regions may not have any fourth generation instance families but have fifth and sixth generation instance families.</p> <p>When using <code>default_x86_64</code> or <code>default_arm64</code> instance bundles, Batch selects instance families based on a balance of cost-effectiveness and performance. While newer generation instances often provide better price-performance, Batch may choose an earlier generation instance family if it provides the optimal combination of availability, cost, and performance for your workload. For example, in an Amazon Web Services Region where both c6i and c7i instances are available, Batch might select c6i instances if they offer better cost-effectiveness for your specific job requirements. For more information on Batch instance types and Amazon Web Services Region availability, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/instance-type-compute-table.html\">Instance type compute table</a> in the <i>Batch User Guide</i>.</p> <p>Batch periodically updates your instances in default bundles to newer, more cost-effective options. Updates happen automatically without requiring any action from you. Your workloads continue running during updates with no interruption </p> </note> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note> <note> <p>When you create a compute environment, the instance types that you select for the compute environment must share the same architecture. For example, you can't mix x86 and ARM instances in the same compute environment.</p> </note>"""
    image_id: NotRequired["aws_sdk_batch.types.string.String"]
    r"""<p>The Amazon Machine Image (AMI) ID used for instances launched in the compute environment. This parameter is overridden by the <code>imageIdOverride</code> member of the <code>Ec2Configuration</code> structure.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note> <note> <p>The AMI that you choose for a compute environment must match the architecture of the instance types that you intend to use for that compute environment. For example, if your compute environment uses A1 instance types, the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the Amazon ECS-optimized Amazon Linux 2023 AMI. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html#ecs-optimized-ami-linux-variants.html\">Amazon ECS-optimized Amazon Linux 2023 AMI</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> </note>"""
    subnets: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    r"""<p>The VPC subnets where the compute resources are launched. These subnets must be within the same VPC. Fargate compute resources can contain up to 16 subnets. For more information, see <a href=\"https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html\">VPCs and subnets</a> in the <i>Amazon VPC User Guide</i>.</p> <note> <p>Batch on Amazon EC2 and Batch on Amazon EKS support Local Zones. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones\"> Local Zones</a> in the <i>Amazon EC2 User Guide for Linux Instances</i>, <a href=\"https://docs.aws.amazon.com/eks/latest/userguide/local-zones.html\">Amazon EKS and Amazon Web Services Local Zones</a> in the <i>Amazon EKS User Guide</i> and <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-regions-zones.html#clusters-local-zones\"> Amazon ECS clusters in Local Zones, Wavelength Zones, and Amazon Web Services Outposts</a> in the <i>Amazon ECS Developer Guide</i>.</p> <p>Batch on Fargate doesn't currently support Local Zones.</p> </note>"""
    security_group_ids: NotRequired["aws_sdk_batch.types.string_list.StringList"]
    """<p>The Amazon EC2 security groups that are associated with instances launched in the compute environment. One or more security groups must be specified, either in <code>securityGroupIds</code> or using a launch template referenced in <code>launchTemplate</code>. This parameter is required for jobs that are running on Fargate resources and must contain at least one security group. Fargate doesn't support launch templates. If security groups are specified using both <code>securityGroupIds</code> and <code>launchTemplate</code>, the values in <code>securityGroupIds</code> are used.</p>"""
    ec2_key_pair: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon EC2 key pair that's used for instances launched in the compute environment. You can use this key pair to log in to your instances with SSH.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    instance_role: NotRequired["aws_sdk_batch.types.string.String"]
    r"""<p>The Amazon ECS instance profile applied to Amazon EC2 instances in a compute environment. This parameter is required for Amazon EC2 instances types. You can specify the short name or full Amazon Resource Name (ARN) of an instance profile. For example, <code> <i>ecsInstanceRole</i> </code> or <code>arn:aws:iam::<i><aws_account_id></i>:instance-profile/<i>ecsInstanceRole</i> </code>. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/instance_IAM_role.html\">Amazon ECS instance role</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    tags: NotRequired["aws_sdk_batch.types.tags_map.TagsMap"]
    r"""<p>Key-value pair tags to be applied to Amazon EC2 resources that are launched in the compute environment. For Batch, these take the form of <code>\"String1\": \"String2\"</code>, where <code>String1</code> is the tag key and <code>String2</code> is the tag value (for example, <code>{ \"Name\": \"Batch Instance - C4OnDemand\" }</code>). This is helpful for recognizing your Batch instances in the Amazon EC2 console. Updating these tags requires an infrastructure update to the compute environment. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/updating-compute-environments.html\">Updating compute environments</a> in the <i>Batch User Guide</i>. These tags aren't seen when using the Batch <code>ListTagsForResource</code> API operation.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    placement_group: NotRequired["aws_sdk_batch.types.string.String"]
    r"""<p>The Amazon EC2 placement group to associate with your compute resources. If you intend to submit multi-node parallel jobs to your compute environment, you should consider creating a cluster placement group and associate it with your compute resources. This keeps your multi-node parallel job on a logical grouping of instances within a single Availability Zone with high network flow potential. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html\">Placement groups</a> in the <i>Amazon EC2 User Guide for Linux Instances</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    bid_percentage: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The maximum percentage that a Spot Instance price can be when compared with the On-Demand price for that instance type before instances are launched. For example, if your maximum percentage is 20%, then the Spot price must be less than 20% of the current On-Demand price for that Amazon EC2 instance. You always pay the lowest (market) price and never more than your maximum percentage. If you leave this field empty, the default value is 100% of the On-Demand price. For most use cases, we recommend leaving this field empty.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    spot_iam_fleet_role: NotRequired["aws_sdk_batch.types.string.String"]
    r"""<p>The Amazon Resource Name (ARN) of the Amazon EC2 Spot Fleet IAM role applied to a <code>SPOT</code> compute environment. This role is required if the allocation strategy set to <code>BEST_FIT</code> or if the allocation strategy isn't specified. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/spot_fleet_IAM_role.html\">Amazon EC2 spot fleet role</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note> <important> <p>To tag your Spot Instances on creation, the Spot Fleet IAM role specified here must use the newer <b>AmazonEC2SpotFleetTaggingRole</b> managed policy. The previously recommended <b>AmazonEC2SpotFleetRole</b> managed policy doesn't have the required permissions to tag Spot Instances. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/troubleshooting.html#spot-instance-no-tag\">Spot instances not tagged on creation</a> in the <i>Batch User Guide</i>.</p> </important>"""
    launch_template: NotRequired[
        "aws_sdk_batch.types.launch_template_specification.LaunchTemplateSpecification"
    ]
    r"""<p>The launch template to use for your compute resources. Any other compute resource parameters that you specify in a <a href=\"https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html\">CreateComputeEnvironment</a> API operation override the same parameters in the launch template. You must specify either the launch template ID or launch template name in the request, but not both. For more information, see <a href=\"https://docs.aws.amazon.com/batch/latest/userguide/launch-templates.html\">Launch template support</a> in the <i>Batch User Guide</i>.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    ec2_configuration: NotRequired[
        "aws_sdk_batch.types.ec2_configuration_list.Ec2ConfigurationList"
    ]
    """<p>Provides information that's used to select Amazon Machine Images (AMIs) for Amazon EC2 instances in the compute environment. If <code>Ec2Configuration</code> isn't specified, the default is <code>ECS_AL2023</code> for EC2 (ECS) compute environments and <code>EKS_AL2023</code> for EKS compute environments.</p> <p>One or two values can be provided.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""
    scaling_policy: NotRequired[
        "aws_sdk_batch.types.compute_scaling_policy.ComputeScalingPolicy"
    ]
    """<p>The scaling policy configuration for the compute environment.</p> <note> <p>This parameter isn't applicable to jobs that are running on Fargate resources. Don't specify it.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeResource) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_batch.types.cr_type

        out["type"] = aws_sdk_batch.types.cr_type.serialize_json(value["type"])
    if "allocation_strategy" in value:
        import aws_sdk_batch.types.cr_allocation_strategy

        out["allocationStrategy"] = (
            aws_sdk_batch.types.cr_allocation_strategy.serialize_json(
                value["allocation_strategy"]
            )
        )
    if "minv_cpus" in value:
        out["minvCpus"] = value["minv_cpus"]
    if "maxv_cpus" in value:
        out["maxvCpus"] = value["maxv_cpus"]
    if "desiredv_cpus" in value:
        out["desiredvCpus"] = value["desiredv_cpus"]
    if "instance_types" in value:
        import aws_sdk_batch.types.string_list

        out["instanceTypes"] = aws_sdk_batch.types.string_list.serialize_json(
            value["instance_types"]
        )
    if "image_id" in value:
        out["imageId"] = value["image_id"]
    if "subnets" in value:
        import aws_sdk_batch.types.string_list

        out["subnets"] = aws_sdk_batch.types.string_list.serialize_json(
            value["subnets"]
        )
    if "security_group_ids" in value:
        import aws_sdk_batch.types.string_list

        out["securityGroupIds"] = aws_sdk_batch.types.string_list.serialize_json(
            value["security_group_ids"]
        )
    if "ec2_key_pair" in value:
        out["ec2KeyPair"] = value["ec2_key_pair"]
    if "instance_role" in value:
        out["instanceRole"] = value["instance_role"]
    if "tags" in value:
        import aws_sdk_batch.types.tags_map

        out["tags"] = aws_sdk_batch.types.tags_map.serialize_json(value["tags"])
    if "placement_group" in value:
        out["placementGroup"] = value["placement_group"]
    if "bid_percentage" in value:
        out["bidPercentage"] = value["bid_percentage"]
    if "spot_iam_fleet_role" in value:
        out["spotIamFleetRole"] = value["spot_iam_fleet_role"]
    if "launch_template" in value:
        import aws_sdk_batch.types.launch_template_specification

        out["launchTemplate"] = (
            aws_sdk_batch.types.launch_template_specification.serialize_json(
                value["launch_template"]
            )
        )
    if "ec2_configuration" in value:
        import aws_sdk_batch.types.ec2_configuration_list

        out["ec2Configuration"] = (
            aws_sdk_batch.types.ec2_configuration_list.serialize_json(
                value["ec2_configuration"]
            )
        )
    if "scaling_policy" in value:
        import aws_sdk_batch.types.compute_scaling_policy

        out["scalingPolicy"] = (
            aws_sdk_batch.types.compute_scaling_policy.serialize_json(
                value["scaling_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComputeResource:
    out: ComputeResource = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_batch.types.cr_type

        out["type"] = aws_sdk_batch.types.cr_type.deserialize_json(data["type"])
    if "allocationStrategy" in data:
        import aws_sdk_batch.types.cr_allocation_strategy

        out["allocation_strategy"] = (
            aws_sdk_batch.types.cr_allocation_strategy.deserialize_json(
                data["allocationStrategy"]
            )
        )
    if "minvCpus" in data:
        out["minv_cpus"] = data["minvCpus"]
    if "maxvCpus" in data:
        out["maxv_cpus"] = data["maxvCpus"]
    if "desiredvCpus" in data:
        out["desiredv_cpus"] = data["desiredvCpus"]
    if "instanceTypes" in data:
        import aws_sdk_batch.types.string_list

        out["instance_types"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["instanceTypes"]
        )
    if "imageId" in data:
        out["image_id"] = data["imageId"]
    if "subnets" in data:
        import aws_sdk_batch.types.string_list

        out["subnets"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["subnets"]
        )
    if "securityGroupIds" in data:
        import aws_sdk_batch.types.string_list

        out["security_group_ids"] = aws_sdk_batch.types.string_list.deserialize_json(
            data["securityGroupIds"]
        )
    if "ec2KeyPair" in data:
        out["ec2_key_pair"] = data["ec2KeyPair"]
    if "instanceRole" in data:
        out["instance_role"] = data["instanceRole"]
    if "tags" in data:
        import aws_sdk_batch.types.tags_map

        out["tags"] = aws_sdk_batch.types.tags_map.deserialize_json(data["tags"])
    if "placementGroup" in data:
        out["placement_group"] = data["placementGroup"]
    if "bidPercentage" in data:
        out["bid_percentage"] = data["bidPercentage"]
    if "spotIamFleetRole" in data:
        out["spot_iam_fleet_role"] = data["spotIamFleetRole"]
    if "launchTemplate" in data:
        import aws_sdk_batch.types.launch_template_specification

        out["launch_template"] = (
            aws_sdk_batch.types.launch_template_specification.deserialize_json(
                data["launchTemplate"]
            )
        )
    if "ec2Configuration" in data:
        import aws_sdk_batch.types.ec2_configuration_list

        out["ec2_configuration"] = (
            aws_sdk_batch.types.ec2_configuration_list.deserialize_json(
                data["ec2Configuration"]
            )
        )
    if "scalingPolicy" in data:
        import aws_sdk_batch.types.compute_scaling_policy

        out["scaling_policy"] = (
            aws_sdk_batch.types.compute_scaling_policy.deserialize_json(
                data["scalingPolicy"]
            )
        )
    return out
