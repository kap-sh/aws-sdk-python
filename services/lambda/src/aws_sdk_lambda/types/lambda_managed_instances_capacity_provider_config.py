"""Generated from Smithy shape ``com.amazonaws.lambda#LambdaManagedInstancesCapacityProviderConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_arn
    import aws_sdk_lambda.types.execution_environment_memory_gi_b_per_v_cpu
    import aws_sdk_lambda.types.per_execution_environment_max_concurrency


class LambdaManagedInstancesCapacityProviderConfig(TypedDict):
    capacity_provider_arn: (
        "aws_sdk_lambda.types.capacity_provider_arn.CapacityProviderArn"
    )
    """<p>The Amazon Resource Name (ARN) of the capacity provider.</p>"""
    per_execution_environment_max_concurrency: NotRequired[
        "aws_sdk_lambda.types.per_execution_environment_max_concurrency.PerExecutionEnvironmentMaxConcurrency"
    ]
    """<p>The maximum number of concurrent execution environments that can run on each compute instance.</p>"""
    execution_environment_memory_gi_b_per_v_cpu: NotRequired[
        "aws_sdk_lambda.types.execution_environment_memory_gi_b_per_v_cpu.ExecutionEnvironmentMemoryGiBPerVCpu"
    ]
    """<p>The amount of memory in GiB allocated per vCPU for execution environments.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LambdaManagedInstancesCapacityProviderConfig) -> dict:
    out: dict = {}
    out["CapacityProviderArn"] = value["capacity_provider_arn"]
    if "per_execution_environment_max_concurrency" in value:
        out["PerExecutionEnvironmentMaxConcurrency"] = value[
            "per_execution_environment_max_concurrency"
        ]
    if "execution_environment_memory_gi_b_per_v_cpu" in value:
        out["ExecutionEnvironmentMemoryGiBPerVCpu"] = value[
            "execution_environment_memory_gi_b_per_v_cpu"
        ]
    return out


def deserialize_json(data: dict) -> LambdaManagedInstancesCapacityProviderConfig:
    out: LambdaManagedInstancesCapacityProviderConfig = {}  # type: ignore[typeddict-item]
    if "CapacityProviderArn" in data:
        out["capacity_provider_arn"] = data["CapacityProviderArn"]
    else:
        raise DeserializationError(
            "LambdaManagedInstancesCapacityProviderConfig.capacity_provider_arn required"
        )
    if "PerExecutionEnvironmentMaxConcurrency" in data:
        out["per_execution_environment_max_concurrency"] = data[
            "PerExecutionEnvironmentMaxConcurrency"
        ]
    if "ExecutionEnvironmentMemoryGiBPerVCpu" in data:
        out["execution_environment_memory_gi_b_per_v_cpu"] = data[
            "ExecutionEnvironmentMemoryGiBPerVCpu"
        ]
    return out
