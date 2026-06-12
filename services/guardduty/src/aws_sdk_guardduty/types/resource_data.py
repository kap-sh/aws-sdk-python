"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.access_key
    import aws_sdk_guardduty.types.autoscaling_auto_scaling_group
    import aws_sdk_guardduty.types.cloudformation_stack
    import aws_sdk_guardduty.types.container_finding_resource
    import aws_sdk_guardduty.types.ec2_image
    import aws_sdk_guardduty.types.ec2_instance
    import aws_sdk_guardduty.types.ec2_launch_template
    import aws_sdk_guardduty.types.ec2_network_interface
    import aws_sdk_guardduty.types.ec2_vpc
    import aws_sdk_guardduty.types.ecs_cluster
    import aws_sdk_guardduty.types.ecs_task
    import aws_sdk_guardduty.types.eks_cluster
    import aws_sdk_guardduty.types.iam_instance_profile_v2
    import aws_sdk_guardduty.types.kubernetes_workload
    import aws_sdk_guardduty.types.s3_bucket
    import aws_sdk_guardduty.types.s3_object


class ResourceData(TypedDict):
    s3_bucket: NotRequired["aws_sdk_guardduty.types.s3_bucket.S3Bucket"]
    """<p>Contains information about the Amazon S3 bucket.</p>"""
    ec2_instance: NotRequired["aws_sdk_guardduty.types.ec2_instance.Ec2Instance"]
    """<p>Contains information about the Amazon EC2 instance.</p>"""
    access_key: NotRequired["aws_sdk_guardduty.types.access_key.AccessKey"]
    """<p>Contains information about the IAM access key details of a user that involved in the GuardDuty finding.</p>"""
    ec2_network_interface: NotRequired[
        "aws_sdk_guardduty.types.ec2_network_interface.Ec2NetworkInterface"
    ]
    """<p>Contains information about the elastic network interface of the Amazon EC2 instance.</p>"""
    s3_object: NotRequired["aws_sdk_guardduty.types.s3_object.S3Object"]
    """<p>Contains information about the Amazon S3 object.</p>"""
    eks_cluster: NotRequired["aws_sdk_guardduty.types.eks_cluster.EksCluster"]
    """<p>Contains detailed information about the Amazon EKS cluster associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    kubernetes_workload: NotRequired[
        "aws_sdk_guardduty.types.kubernetes_workload.KubernetesWorkload"
    ]
    """<p>Contains detailed information about the Kubernetes workload associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    container: NotRequired[
        "aws_sdk_guardduty.types.container_finding_resource.ContainerFindingResource"
    ]
    """<p>Contains detailed information about the container associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ecs_cluster: NotRequired["aws_sdk_guardduty.types.ecs_cluster.EcsCluster"]
    """<p>Contains detailed information about the Amazon ECS cluster associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ecs_task: NotRequired["aws_sdk_guardduty.types.ecs_task.EcsTask"]
    """<p>Contains detailed information about the Amazon ECS task associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    iam_instance_profile: NotRequired[
        "aws_sdk_guardduty.types.iam_instance_profile_v2.IamInstanceProfileV2"
    ]
    """<p>Contains detailed information about the IAM instance profile associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    autoscaling_auto_scaling_group: NotRequired[
        "aws_sdk_guardduty.types.autoscaling_auto_scaling_group.AutoscalingAutoScalingGroup"
    ]
    """<p>Contains detailed information about the Auto Scaling Group associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ec2_launch_template: NotRequired[
        "aws_sdk_guardduty.types.ec2_launch_template.Ec2LaunchTemplate"
    ]
    """<p>Contains detailed information about the EC2 launch template associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ec2_vpc: NotRequired["aws_sdk_guardduty.types.ec2_vpc.Ec2Vpc"]
    """<p>Contains detailed information about the EC2 VPC associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    ec2_image: NotRequired["aws_sdk_guardduty.types.ec2_image.Ec2Image"]
    """<p>Contains detailed information about the EC2 Image associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    cloudformation_stack: NotRequired[
        "aws_sdk_guardduty.types.cloudformation_stack.CloudformationStack"
    ]
    """<p>Contains detailed information about the CloudFormation stack associated with the activity that prompted GuardDuty to generate a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceData) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        import aws_sdk_guardduty.types.s3_bucket

        out["s3Bucket"] = aws_sdk_guardduty.types.s3_bucket.serialize_json(
            value["s3_bucket"]
        )
    if "ec2_instance" in value:
        import aws_sdk_guardduty.types.ec2_instance

        out["ec2Instance"] = aws_sdk_guardduty.types.ec2_instance.serialize_json(
            value["ec2_instance"]
        )
    if "access_key" in value:
        import aws_sdk_guardduty.types.access_key

        out["accessKey"] = aws_sdk_guardduty.types.access_key.serialize_json(
            value["access_key"]
        )
    if "ec2_network_interface" in value:
        import aws_sdk_guardduty.types.ec2_network_interface

        out["ec2NetworkInterface"] = (
            aws_sdk_guardduty.types.ec2_network_interface.serialize_json(
                value["ec2_network_interface"]
            )
        )
    if "s3_object" in value:
        import aws_sdk_guardduty.types.s3_object

        out["s3Object"] = aws_sdk_guardduty.types.s3_object.serialize_json(
            value["s3_object"]
        )
    if "eks_cluster" in value:
        import aws_sdk_guardduty.types.eks_cluster

        out["eksCluster"] = aws_sdk_guardduty.types.eks_cluster.serialize_json(
            value["eks_cluster"]
        )
    if "kubernetes_workload" in value:
        import aws_sdk_guardduty.types.kubernetes_workload

        out["kubernetesWorkload"] = (
            aws_sdk_guardduty.types.kubernetes_workload.serialize_json(
                value["kubernetes_workload"]
            )
        )
    if "container" in value:
        import aws_sdk_guardduty.types.container_finding_resource

        out["container"] = (
            aws_sdk_guardduty.types.container_finding_resource.serialize_json(
                value["container"]
            )
        )
    if "ecs_cluster" in value:
        import aws_sdk_guardduty.types.ecs_cluster

        out["ecsCluster"] = aws_sdk_guardduty.types.ecs_cluster.serialize_json(
            value["ecs_cluster"]
        )
    if "ecs_task" in value:
        import aws_sdk_guardduty.types.ecs_task

        out["ecsTask"] = aws_sdk_guardduty.types.ecs_task.serialize_json(
            value["ecs_task"]
        )
    if "iam_instance_profile" in value:
        import aws_sdk_guardduty.types.iam_instance_profile_v2

        out["iamInstanceProfile"] = (
            aws_sdk_guardduty.types.iam_instance_profile_v2.serialize_json(
                value["iam_instance_profile"]
            )
        )
    if "autoscaling_auto_scaling_group" in value:
        import aws_sdk_guardduty.types.autoscaling_auto_scaling_group

        out["autoscalingAutoScalingGroup"] = (
            aws_sdk_guardduty.types.autoscaling_auto_scaling_group.serialize_json(
                value["autoscaling_auto_scaling_group"]
            )
        )
    if "ec2_launch_template" in value:
        import aws_sdk_guardduty.types.ec2_launch_template

        out["ec2LaunchTemplate"] = (
            aws_sdk_guardduty.types.ec2_launch_template.serialize_json(
                value["ec2_launch_template"]
            )
        )
    if "ec2_vpc" in value:
        import aws_sdk_guardduty.types.ec2_vpc

        out["ec2Vpc"] = aws_sdk_guardduty.types.ec2_vpc.serialize_json(value["ec2_vpc"])
    if "ec2_image" in value:
        import aws_sdk_guardduty.types.ec2_image

        out["ec2Image"] = aws_sdk_guardduty.types.ec2_image.serialize_json(
            value["ec2_image"]
        )
    if "cloudformation_stack" in value:
        import aws_sdk_guardduty.types.cloudformation_stack

        out["cloudformationStack"] = (
            aws_sdk_guardduty.types.cloudformation_stack.serialize_json(
                value["cloudformation_stack"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceData:
    out: ResourceData = {}  # type: ignore[typeddict-item]
    if "s3Bucket" in data:
        import aws_sdk_guardduty.types.s3_bucket

        out["s3_bucket"] = aws_sdk_guardduty.types.s3_bucket.deserialize_json(
            data["s3Bucket"]
        )
    if "ec2Instance" in data:
        import aws_sdk_guardduty.types.ec2_instance

        out["ec2_instance"] = aws_sdk_guardduty.types.ec2_instance.deserialize_json(
            data["ec2Instance"]
        )
    if "accessKey" in data:
        import aws_sdk_guardduty.types.access_key

        out["access_key"] = aws_sdk_guardduty.types.access_key.deserialize_json(
            data["accessKey"]
        )
    if "ec2NetworkInterface" in data:
        import aws_sdk_guardduty.types.ec2_network_interface

        out["ec2_network_interface"] = (
            aws_sdk_guardduty.types.ec2_network_interface.deserialize_json(
                data["ec2NetworkInterface"]
            )
        )
    if "s3Object" in data:
        import aws_sdk_guardduty.types.s3_object

        out["s3_object"] = aws_sdk_guardduty.types.s3_object.deserialize_json(
            data["s3Object"]
        )
    if "eksCluster" in data:
        import aws_sdk_guardduty.types.eks_cluster

        out["eks_cluster"] = aws_sdk_guardduty.types.eks_cluster.deserialize_json(
            data["eksCluster"]
        )
    if "kubernetesWorkload" in data:
        import aws_sdk_guardduty.types.kubernetes_workload

        out["kubernetes_workload"] = (
            aws_sdk_guardduty.types.kubernetes_workload.deserialize_json(
                data["kubernetesWorkload"]
            )
        )
    if "container" in data:
        import aws_sdk_guardduty.types.container_finding_resource

        out["container"] = (
            aws_sdk_guardduty.types.container_finding_resource.deserialize_json(
                data["container"]
            )
        )
    if "ecsCluster" in data:
        import aws_sdk_guardduty.types.ecs_cluster

        out["ecs_cluster"] = aws_sdk_guardduty.types.ecs_cluster.deserialize_json(
            data["ecsCluster"]
        )
    if "ecsTask" in data:
        import aws_sdk_guardduty.types.ecs_task

        out["ecs_task"] = aws_sdk_guardduty.types.ecs_task.deserialize_json(
            data["ecsTask"]
        )
    if "iamInstanceProfile" in data:
        import aws_sdk_guardduty.types.iam_instance_profile_v2

        out["iam_instance_profile"] = (
            aws_sdk_guardduty.types.iam_instance_profile_v2.deserialize_json(
                data["iamInstanceProfile"]
            )
        )
    if "autoscalingAutoScalingGroup" in data:
        import aws_sdk_guardduty.types.autoscaling_auto_scaling_group

        out["autoscaling_auto_scaling_group"] = (
            aws_sdk_guardduty.types.autoscaling_auto_scaling_group.deserialize_json(
                data["autoscalingAutoScalingGroup"]
            )
        )
    if "ec2LaunchTemplate" in data:
        import aws_sdk_guardduty.types.ec2_launch_template

        out["ec2_launch_template"] = (
            aws_sdk_guardduty.types.ec2_launch_template.deserialize_json(
                data["ec2LaunchTemplate"]
            )
        )
    if "ec2Vpc" in data:
        import aws_sdk_guardduty.types.ec2_vpc

        out["ec2_vpc"] = aws_sdk_guardduty.types.ec2_vpc.deserialize_json(
            data["ec2Vpc"]
        )
    if "ec2Image" in data:
        import aws_sdk_guardduty.types.ec2_image

        out["ec2_image"] = aws_sdk_guardduty.types.ec2_image.deserialize_json(
            data["ec2Image"]
        )
    if "cloudformationStack" in data:
        import aws_sdk_guardduty.types.cloudformation_stack

        out["cloudformation_stack"] = (
            aws_sdk_guardduty.types.cloudformation_stack.deserialize_json(
                data["cloudformationStack"]
            )
        )
    return out
