"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterKubernetesTaint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sagemaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_kubernetes_taint_effect
    import aws_sdk_sagemaker.types.cluster_kubernetes_taint_key
    import aws_sdk_sagemaker.types.cluster_kubernetes_taint_value


class ClusterKubernetesTaint(TypedDict, closed=True):
    key: (
        "aws_sdk_sagemaker.types.cluster_kubernetes_taint_key.ClusterKubernetesTaintKey"
    )
    """<p>The key of the taint.</p>"""
    value: NotRequired[
        "aws_sdk_sagemaker.types.cluster_kubernetes_taint_value.ClusterKubernetesTaintValue"
    ]
    """<p>The value of the taint.</p>"""
    effect: "aws_sdk_sagemaker.types.cluster_kubernetes_taint_effect.ClusterKubernetesTaintEffect"
    """<p>The effect of the taint. Valid values are <code>NoSchedule</code>, <code>PreferNoSchedule</code>, and <code>NoExecute</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterKubernetesTaint) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    import aws_sdk_sagemaker.types.cluster_kubernetes_taint_effect

    out["Effect"] = (
        aws_sdk_sagemaker.types.cluster_kubernetes_taint_effect.serialize_aws_json_1_1(
            value["effect"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterKubernetesTaint:
    out: ClusterKubernetesTaint = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("ClusterKubernetesTaint.key required")
    if "Value" in data:
        out["value"] = data["Value"]
    if "Effect" in data:
        import aws_sdk_sagemaker.types.cluster_kubernetes_taint_effect

        out["effect"] = (
            aws_sdk_sagemaker.types.cluster_kubernetes_taint_effect.deserialize_aws_json_1_1(
                data["Effect"]
            )
        )
    else:
        raise DeserializationError("ClusterKubernetesTaint.effect required")
    return out
