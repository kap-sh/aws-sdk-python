"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEksWorkloadInfoList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_inspector2.types.aws_eks_workload_info

AwsEksWorkloadInfoList: TypeAlias = list["aws_sdk_inspector2.types.aws_eks_workload_info.AwsEksWorkloadInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEksWorkloadInfoList) -> list:
    import aws_sdk_inspector2.types.aws_eks_workload_info
    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.aws_eks_workload_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> AwsEksWorkloadInfoList:
    import aws_sdk_inspector2.types.aws_eks_workload_info
    out: AwsEksWorkloadInfoList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.aws_eks_workload_info.deserialize_json(item))
    return out