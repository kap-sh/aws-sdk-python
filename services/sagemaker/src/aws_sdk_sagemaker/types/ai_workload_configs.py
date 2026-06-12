"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIWorkloadConfigs``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workload_spec


class AIWorkloadConfigs(TypedDict):
    workload_spec: NotRequired["aws_sdk_sagemaker.types.workload_spec.WorkloadSpec"]
    """<p>The workload specification that defines benchmark parameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIWorkloadConfigs) -> dict:
    out: dict = {}
    if "workload_spec" in value:
        import aws_sdk_sagemaker.types.workload_spec

        out["WorkloadSpec"] = (
            aws_sdk_sagemaker.types.workload_spec.serialize_aws_json_1_1(
                value["workload_spec"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIWorkloadConfigs:
    out: AIWorkloadConfigs = {}  # type: ignore[typeddict-item]
    if "WorkloadSpec" in data:
        import aws_sdk_sagemaker.types.workload_spec

        out["workload_spec"] = (
            aws_sdk_sagemaker.types.workload_spec.deserialize_aws_json_1_1(
                data["WorkloadSpec"]
            )
        )
    return out
