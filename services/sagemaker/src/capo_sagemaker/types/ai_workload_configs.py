"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIWorkloadConfigs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.workload_spec


class AIWorkloadConfigs(TypedDict, closed=True):
    workload_spec: NotRequired["capo_sagemaker.types.workload_spec.WorkloadSpec"]
    """<p>The workload specification that defines benchmark parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIWorkloadConfigs) -> dict:
    out: dict = {}
    if "workload_spec" in value:
        import capo_sagemaker.types.workload_spec

        out["WorkloadSpec"] = capo_sagemaker.types.workload_spec.serialize_aws_json_1_1(
            value["workload_spec"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIWorkloadConfigs:
    out: AIWorkloadConfigs = {}  # type: ignore[typeddict-item]
    if "WorkloadSpec" in data:
        import capo_sagemaker.types.workload_spec

        out["workload_spec"] = (
            capo_sagemaker.types.workload_spec.deserialize_aws_json_1_1(
                data["WorkloadSpec"]
            )
        )
    return out
