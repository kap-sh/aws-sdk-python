"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.eks_role_access_entries


class ClusterMetadata(TypedDict):
    failure_message: NotRequired["str"]
    """<p>An error message describing why the cluster level operation (such as creating, updating, or deleting) failed.</p>"""
    eks_role_access_entries: NotRequired[
        "aws_sdk_sagemaker.types.eks_role_access_entries.EksRoleAccessEntries"
    ]
    """<p>A list of Amazon EKS IAM role ARNs associated with the cluster. This is created by HyperPod on your behalf and only applies for EKS orchestrated clusters.</p>"""
    slr_access_entry: NotRequired["str"]
    """<p>The Service-Linked Role (SLR) associated with the cluster. This is created by HyperPod on your behalf and only applies for EKS orchestrated clusters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterMetadata) -> dict:
    out: dict = {}
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "eks_role_access_entries" in value:
        import aws_sdk_sagemaker.types.eks_role_access_entries

        out["EksRoleAccessEntries"] = (
            aws_sdk_sagemaker.types.eks_role_access_entries.serialize_aws_json_1_1(
                value["eks_role_access_entries"]
            )
        )
    if "slr_access_entry" in value:
        out["SlrAccessEntry"] = value["slr_access_entry"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterMetadata:
    out: ClusterMetadata = {}  # type: ignore[typeddict-item]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "EksRoleAccessEntries" in data:
        import aws_sdk_sagemaker.types.eks_role_access_entries

        out["eks_role_access_entries"] = (
            aws_sdk_sagemaker.types.eks_role_access_entries.deserialize_aws_json_1_1(
                data["EksRoleAccessEntries"]
            )
        )
    if "SlrAccessEntry" in data:
        out["slr_access_entry"] = data["SlrAccessEntry"]
    return out
