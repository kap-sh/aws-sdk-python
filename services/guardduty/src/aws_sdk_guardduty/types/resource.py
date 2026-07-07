"""Generated from Smithy shape ``com.amazonaws.guardduty#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.access_key_details
    import aws_sdk_guardduty.types.container
    import aws_sdk_guardduty.types.ebs_snapshot_details
    import aws_sdk_guardduty.types.ebs_volume_details
    import aws_sdk_guardduty.types.ec2_image_details
    import aws_sdk_guardduty.types.ecs_cluster_details
    import aws_sdk_guardduty.types.eks_cluster_details
    import aws_sdk_guardduty.types.instance_details
    import aws_sdk_guardduty.types.kubernetes_details
    import aws_sdk_guardduty.types.lambda_details
    import aws_sdk_guardduty.types.rds_db_instance_details
    import aws_sdk_guardduty.types.rds_db_user_details
    import aws_sdk_guardduty.types.rds_limitless_db_details
    import aws_sdk_guardduty.types.recovery_point_details
    import aws_sdk_guardduty.types.s3_bucket_details
    import aws_sdk_guardduty.types.string


class Resource(TypedDict, closed=True):
    access_key_details: NotRequired[
        "aws_sdk_guardduty.types.access_key_details.AccessKeyDetails"
    ]
    """<p>The IAM access key details (user information) of a user that engaged in the activity that prompted GuardDuty to generate a finding.</p>"""
    s3_bucket_details: NotRequired[
        "aws_sdk_guardduty.types.s3_bucket_details.S3BucketDetails"
    ]
    """<p>Contains information on the S3 bucket.</p>"""
    instance_details: NotRequired[
        "aws_sdk_guardduty.types.instance_details.InstanceDetails"
    ]
    """<p>The information about the EC2 instance associated with the activity that prompted GuardDuty to generate a finding.</p>"""
    eks_cluster_details: NotRequired[
        "aws_sdk_guardduty.types.eks_cluster_details.EksClusterDetails"
    ]
    """<p>Details about the EKS cluster involved in a Kubernetes finding.</p>"""
    kubernetes_details: NotRequired[
        "aws_sdk_guardduty.types.kubernetes_details.KubernetesDetails"
    ]
    """<p>Details about the Kubernetes user and workload involved in a Kubernetes finding.</p>"""
    resource_type: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The type of Amazon Web Services resource.</p>"""
    ebs_volume_details: NotRequired[
        "aws_sdk_guardduty.types.ebs_volume_details.EbsVolumeDetails"
    ]
    """<p>Contains list of scanned and skipped EBS volumes with details.</p>"""
    ecs_cluster_details: NotRequired[
        "aws_sdk_guardduty.types.ecs_cluster_details.EcsClusterDetails"
    ]
    """<p>Contains information about the details of the ECS Cluster.</p>"""
    container_details: NotRequired["aws_sdk_guardduty.types.container.Container"]
    lambda_details: NotRequired["aws_sdk_guardduty.types.lambda_details.LambdaDetails"]
    """<p>Contains information about the Lambda function that was involved in a finding.</p>"""
    rds_db_instance_details: NotRequired[
        "aws_sdk_guardduty.types.rds_db_instance_details.RdsDbInstanceDetails"
    ]
    """<p>Contains information about the database instance to which an anomalous login attempt was made.</p>"""
    rds_limitless_db_details: NotRequired[
        "aws_sdk_guardduty.types.rds_limitless_db_details.RdsLimitlessDbDetails"
    ]
    """<p>Contains information about the RDS Limitless database that was involved in a GuardDuty finding.</p>"""
    rds_db_user_details: NotRequired[
        "aws_sdk_guardduty.types.rds_db_user_details.RdsDbUserDetails"
    ]
    """<p>Contains information about the user details through which anomalous login attempt was made.</p>"""
    ebs_snapshot_details: NotRequired[
        "aws_sdk_guardduty.types.ebs_snapshot_details.EbsSnapshotDetails"
    ]
    """<p>Contains details about the EBS snapshot that was scanned.</p>"""
    ec2_image_details: NotRequired[
        "aws_sdk_guardduty.types.ec2_image_details.Ec2ImageDetails"
    ]
    """<p>Contains details about the EC2 image that was scanned.</p>"""
    recovery_point_details: NotRequired[
        "aws_sdk_guardduty.types.recovery_point_details.RecoveryPointDetails"
    ]
    """<p>Contains details about the backup recovery point that was scanned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "access_key_details" in value:
        import aws_sdk_guardduty.types.access_key_details

        out["accessKeyDetails"] = (
            aws_sdk_guardduty.types.access_key_details.serialize_json(
                value["access_key_details"]
            )
        )
    if "s3_bucket_details" in value:
        import aws_sdk_guardduty.types.s3_bucket_details

        out["s3BucketDetails"] = (
            aws_sdk_guardduty.types.s3_bucket_details.serialize_json(
                value["s3_bucket_details"]
            )
        )
    if "instance_details" in value:
        import aws_sdk_guardduty.types.instance_details

        out["instanceDetails"] = (
            aws_sdk_guardduty.types.instance_details.serialize_json(
                value["instance_details"]
            )
        )
    if "eks_cluster_details" in value:
        import aws_sdk_guardduty.types.eks_cluster_details

        out["eksClusterDetails"] = (
            aws_sdk_guardduty.types.eks_cluster_details.serialize_json(
                value["eks_cluster_details"]
            )
        )
    if "kubernetes_details" in value:
        import aws_sdk_guardduty.types.kubernetes_details

        out["kubernetesDetails"] = (
            aws_sdk_guardduty.types.kubernetes_details.serialize_json(
                value["kubernetes_details"]
            )
        )
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "ebs_volume_details" in value:
        import aws_sdk_guardduty.types.ebs_volume_details

        out["ebsVolumeDetails"] = (
            aws_sdk_guardduty.types.ebs_volume_details.serialize_json(
                value["ebs_volume_details"]
            )
        )
    if "ecs_cluster_details" in value:
        import aws_sdk_guardduty.types.ecs_cluster_details

        out["ecsClusterDetails"] = (
            aws_sdk_guardduty.types.ecs_cluster_details.serialize_json(
                value["ecs_cluster_details"]
            )
        )
    if "container_details" in value:
        import aws_sdk_guardduty.types.container

        out["containerDetails"] = aws_sdk_guardduty.types.container.serialize_json(
            value["container_details"]
        )
    if "lambda_details" in value:
        import aws_sdk_guardduty.types.lambda_details

        out["lambdaDetails"] = aws_sdk_guardduty.types.lambda_details.serialize_json(
            value["lambda_details"]
        )
    if "rds_db_instance_details" in value:
        import aws_sdk_guardduty.types.rds_db_instance_details

        out["rdsDbInstanceDetails"] = (
            aws_sdk_guardduty.types.rds_db_instance_details.serialize_json(
                value["rds_db_instance_details"]
            )
        )
    if "rds_limitless_db_details" in value:
        import aws_sdk_guardduty.types.rds_limitless_db_details

        out["rdsLimitlessDbDetails"] = (
            aws_sdk_guardduty.types.rds_limitless_db_details.serialize_json(
                value["rds_limitless_db_details"]
            )
        )
    if "rds_db_user_details" in value:
        import aws_sdk_guardduty.types.rds_db_user_details

        out["rdsDbUserDetails"] = (
            aws_sdk_guardduty.types.rds_db_user_details.serialize_json(
                value["rds_db_user_details"]
            )
        )
    if "ebs_snapshot_details" in value:
        import aws_sdk_guardduty.types.ebs_snapshot_details

        out["ebsSnapshotDetails"] = (
            aws_sdk_guardduty.types.ebs_snapshot_details.serialize_json(
                value["ebs_snapshot_details"]
            )
        )
    if "ec2_image_details" in value:
        import aws_sdk_guardduty.types.ec2_image_details

        out["ec2ImageDetails"] = (
            aws_sdk_guardduty.types.ec2_image_details.serialize_json(
                value["ec2_image_details"]
            )
        )
    if "recovery_point_details" in value:
        import aws_sdk_guardduty.types.recovery_point_details

        out["recoveryPointDetails"] = (
            aws_sdk_guardduty.types.recovery_point_details.serialize_json(
                value["recovery_point_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "accessKeyDetails" in data:
        import aws_sdk_guardduty.types.access_key_details

        out["access_key_details"] = (
            aws_sdk_guardduty.types.access_key_details.deserialize_json(
                data["accessKeyDetails"]
            )
        )
    if "s3BucketDetails" in data:
        import aws_sdk_guardduty.types.s3_bucket_details

        out["s3_bucket_details"] = (
            aws_sdk_guardduty.types.s3_bucket_details.deserialize_json(
                data["s3BucketDetails"]
            )
        )
    if "instanceDetails" in data:
        import aws_sdk_guardduty.types.instance_details

        out["instance_details"] = (
            aws_sdk_guardduty.types.instance_details.deserialize_json(
                data["instanceDetails"]
            )
        )
    if "eksClusterDetails" in data:
        import aws_sdk_guardduty.types.eks_cluster_details

        out["eks_cluster_details"] = (
            aws_sdk_guardduty.types.eks_cluster_details.deserialize_json(
                data["eksClusterDetails"]
            )
        )
    if "kubernetesDetails" in data:
        import aws_sdk_guardduty.types.kubernetes_details

        out["kubernetes_details"] = (
            aws_sdk_guardduty.types.kubernetes_details.deserialize_json(
                data["kubernetesDetails"]
            )
        )
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "ebsVolumeDetails" in data:
        import aws_sdk_guardduty.types.ebs_volume_details

        out["ebs_volume_details"] = (
            aws_sdk_guardduty.types.ebs_volume_details.deserialize_json(
                data["ebsVolumeDetails"]
            )
        )
    if "ecsClusterDetails" in data:
        import aws_sdk_guardduty.types.ecs_cluster_details

        out["ecs_cluster_details"] = (
            aws_sdk_guardduty.types.ecs_cluster_details.deserialize_json(
                data["ecsClusterDetails"]
            )
        )
    if "containerDetails" in data:
        import aws_sdk_guardduty.types.container

        out["container_details"] = aws_sdk_guardduty.types.container.deserialize_json(
            data["containerDetails"]
        )
    if "lambdaDetails" in data:
        import aws_sdk_guardduty.types.lambda_details

        out["lambda_details"] = aws_sdk_guardduty.types.lambda_details.deserialize_json(
            data["lambdaDetails"]
        )
    if "rdsDbInstanceDetails" in data:
        import aws_sdk_guardduty.types.rds_db_instance_details

        out["rds_db_instance_details"] = (
            aws_sdk_guardduty.types.rds_db_instance_details.deserialize_json(
                data["rdsDbInstanceDetails"]
            )
        )
    if "rdsLimitlessDbDetails" in data:
        import aws_sdk_guardduty.types.rds_limitless_db_details

        out["rds_limitless_db_details"] = (
            aws_sdk_guardduty.types.rds_limitless_db_details.deserialize_json(
                data["rdsLimitlessDbDetails"]
            )
        )
    if "rdsDbUserDetails" in data:
        import aws_sdk_guardduty.types.rds_db_user_details

        out["rds_db_user_details"] = (
            aws_sdk_guardduty.types.rds_db_user_details.deserialize_json(
                data["rdsDbUserDetails"]
            )
        )
    if "ebsSnapshotDetails" in data:
        import aws_sdk_guardduty.types.ebs_snapshot_details

        out["ebs_snapshot_details"] = (
            aws_sdk_guardduty.types.ebs_snapshot_details.deserialize_json(
                data["ebsSnapshotDetails"]
            )
        )
    if "ec2ImageDetails" in data:
        import aws_sdk_guardduty.types.ec2_image_details

        out["ec2_image_details"] = (
            aws_sdk_guardduty.types.ec2_image_details.deserialize_json(
                data["ec2ImageDetails"]
            )
        )
    if "recoveryPointDetails" in data:
        import aws_sdk_guardduty.types.recovery_point_details

        out["recovery_point_details"] = (
            aws_sdk_guardduty.types.recovery_point_details.deserialize_json(
                data["recoveryPointDetails"]
            )
        )
    return out
