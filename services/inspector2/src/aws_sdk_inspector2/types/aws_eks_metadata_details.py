"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEksMetadataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.aws_eks_workload_info_list


class AwsEksMetadataDetails(TypedDict, closed=True):
    namespace: NotRequired["str"]
    """<p>The namespace for an Amazon EKS cluster.</p>"""
    workload_info_list: NotRequired[
        "aws_sdk_inspector2.types.aws_eks_workload_info_list.AwsEksWorkloadInfoList"
    ]
    """<p>The list of workloads.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEksMetadataDetails) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "workload_info_list" in value:
        import aws_sdk_inspector2.types.aws_eks_workload_info_list

        out["workloadInfoList"] = (
            aws_sdk_inspector2.types.aws_eks_workload_info_list.serialize_json(
                value["workload_info_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEksMetadataDetails:
    out: AwsEksMetadataDetails = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "workloadInfoList" in data:
        import aws_sdk_inspector2.types.aws_eks_workload_info_list

        out["workload_info_list"] = (
            aws_sdk_inspector2.types.aws_eks_workload_info_list.deserialize_json(
                data["workloadInfoList"]
            )
        )
    return out
