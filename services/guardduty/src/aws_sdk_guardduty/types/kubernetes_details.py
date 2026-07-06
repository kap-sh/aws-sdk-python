"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.kubernetes_user_details
    import aws_sdk_guardduty.types.kubernetes_workload_details


class KubernetesDetails(TypedDict, closed=True):
    kubernetes_user_details: NotRequired[
        "aws_sdk_guardduty.types.kubernetes_user_details.KubernetesUserDetails"
    ]
    """<p>Details about the Kubernetes user involved in a Kubernetes finding.</p>"""
    kubernetes_workload_details: NotRequired[
        "aws_sdk_guardduty.types.kubernetes_workload_details.KubernetesWorkloadDetails"
    ]
    """<p>Details about the Kubernetes workload involved in a Kubernetes finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesDetails) -> dict:
    out: dict = {}
    if "kubernetes_user_details" in value:
        import aws_sdk_guardduty.types.kubernetes_user_details

        out["kubernetesUserDetails"] = (
            aws_sdk_guardduty.types.kubernetes_user_details.serialize_json(
                value["kubernetes_user_details"]
            )
        )
    if "kubernetes_workload_details" in value:
        import aws_sdk_guardduty.types.kubernetes_workload_details

        out["kubernetesWorkloadDetails"] = (
            aws_sdk_guardduty.types.kubernetes_workload_details.serialize_json(
                value["kubernetes_workload_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> KubernetesDetails:
    out: KubernetesDetails = {}  # type: ignore[typeddict-item]
    if "kubernetesUserDetails" in data:
        import aws_sdk_guardduty.types.kubernetes_user_details

        out["kubernetes_user_details"] = (
            aws_sdk_guardduty.types.kubernetes_user_details.deserialize_json(
                data["kubernetesUserDetails"]
            )
        )
    if "kubernetesWorkloadDetails" in data:
        import aws_sdk_guardduty.types.kubernetes_workload_details

        out["kubernetes_workload_details"] = (
            aws_sdk_guardduty.types.kubernetes_workload_details.deserialize_json(
                data["kubernetesWorkloadDetails"]
            )
        )
    return out
