"""Generated from Smithy shape ``com.amazonaws.eks#NodegroupIssueCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

NodegroupIssueCode: TypeAlias = Literal[
    "AutoScalingGroupNotFound",
    "AutoScalingGroupInvalidConfiguration",
    "Ec2SecurityGroupNotFound",
    "Ec2SecurityGroupDeletionFailure",
    "Ec2LaunchTemplateNotFound",
    "Ec2LaunchTemplateVersionMismatch",
    "Ec2SubnetNotFound",
    "Ec2SubnetInvalidConfiguration",
    "IamInstanceProfileNotFound",
    "Ec2SubnetMissingIpv6Assignment",
    "IamLimitExceeded",
    "IamNodeRoleNotFound",
    "NodeCreationFailure",
    "AsgInstanceLaunchFailures",
    "InstanceLimitExceeded",
    "InsufficientFreeAddresses",
    "AccessDenied",
    "InternalFailure",
    "ClusterUnreachable",
    "AmiIdNotFound",
    "AutoScalingGroupOptInRequired",
    "AutoScalingGroupRateLimitExceeded",
    "Ec2LaunchTemplateDeletionFailure",
    "Ec2LaunchTemplateInvalidConfiguration",
    "Ec2LaunchTemplateMaxLimitExceeded",
    "Ec2SubnetListTooLong",
    "IamThrottling",
    "NodeTerminationFailure",
    "PodEvictionFailure",
    "SourceEc2LaunchTemplateNotFound",
    "LimitExceeded",
    "Unknown",
    "AutoScalingGroupInstanceRefreshActive",
    "KubernetesLabelInvalid",
    "Ec2LaunchTemplateVersionMaxLimitExceeded",
    "Ec2InstanceTypeDoesNotExist",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AutoScalingGroupNotFound",
        "AutoScalingGroupInvalidConfiguration",
        "Ec2SecurityGroupNotFound",
        "Ec2SecurityGroupDeletionFailure",
        "Ec2LaunchTemplateNotFound",
        "Ec2LaunchTemplateVersionMismatch",
        "Ec2SubnetNotFound",
        "Ec2SubnetInvalidConfiguration",
        "IamInstanceProfileNotFound",
        "Ec2SubnetMissingIpv6Assignment",
        "IamLimitExceeded",
        "IamNodeRoleNotFound",
        "NodeCreationFailure",
        "AsgInstanceLaunchFailures",
        "InstanceLimitExceeded",
        "InsufficientFreeAddresses",
        "AccessDenied",
        "InternalFailure",
        "ClusterUnreachable",
        "AmiIdNotFound",
        "AutoScalingGroupOptInRequired",
        "AutoScalingGroupRateLimitExceeded",
        "Ec2LaunchTemplateDeletionFailure",
        "Ec2LaunchTemplateInvalidConfiguration",
        "Ec2LaunchTemplateMaxLimitExceeded",
        "Ec2SubnetListTooLong",
        "IamThrottling",
        "NodeTerminationFailure",
        "PodEvictionFailure",
        "SourceEc2LaunchTemplateNotFound",
        "LimitExceeded",
        "Unknown",
        "AutoScalingGroupInstanceRefreshActive",
        "KubernetesLabelInvalid",
        "Ec2LaunchTemplateVersionMaxLimitExceeded",
        "Ec2InstanceTypeDoesNotExist",
    )
)


def serialize_json(value: NodegroupIssueCode) -> str:
    return value


def deserialize_json(data: str) -> NodegroupIssueCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodegroupIssueCode value: {data!r}")
    return cast(NodegroupIssueCode, data)
