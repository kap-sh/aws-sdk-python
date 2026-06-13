"""Generated from Smithy shape ``com.amazonaws.datazone#HyperPodPropertiesOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.hyper_pod_orchestrator


class HyperPodPropertiesOutput(TypedDict):
    cluster_name: "str"
    """<p>The cluster name the hyper pod properties.</p>"""
    cluster_arn: NotRequired["str"]
    """<p>The cluster ARN of the hyper pod properties.</p>"""
    orchestrator: NotRequired[
        "aws_sdk_datazone.types.hyper_pod_orchestrator.HyperPodOrchestrator"
    ]
    """<p>The orchestrator of the hyper pod properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HyperPodPropertiesOutput) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "orchestrator" in value:
        import aws_sdk_datazone.types.hyper_pod_orchestrator

        out["orchestrator"] = (
            aws_sdk_datazone.types.hyper_pod_orchestrator.serialize_json(
                value["orchestrator"]
            )
        )
    return out


def deserialize_json(data: dict) -> HyperPodPropertiesOutput:
    out: HyperPodPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    else:
        raise DeserializationError("HyperPodPropertiesOutput.cluster_name required")
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "orchestrator" in data:
        import aws_sdk_datazone.types.hyper_pod_orchestrator

        out["orchestrator"] = (
            aws_sdk_datazone.types.hyper_pod_orchestrator.deserialize_json(
                data["orchestrator"]
            )
        )
    return out
