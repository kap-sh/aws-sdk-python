"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ContainerRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.container_name
    import aws_sdk_compute_optimizer.types.memory_size_configuration
    import aws_sdk_compute_optimizer.types.nullable_cpu


class ContainerRecommendation(TypedDict):
    container_name: NotRequired[
        "aws_sdk_compute_optimizer.types.container_name.ContainerName"
    ]
    """<p> The name of the container. </p>"""
    memory_size_configuration: NotRequired[
        "aws_sdk_compute_optimizer.types.memory_size_configuration.MemorySizeConfiguration"
    ]
    """<p> The recommended memory size configurations for the container. </p>"""
    cpu: NotRequired["aws_sdk_compute_optimizer.types.nullable_cpu.NullableCpu"]
    """<p> The recommended number of CPU units reserved for the container. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerRecommendation) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "memory_size_configuration" in value:
        import aws_sdk_compute_optimizer.types.memory_size_configuration

        out["memorySizeConfiguration"] = (
            aws_sdk_compute_optimizer.types.memory_size_configuration.serialize_aws_json_1_0(
                value["memory_size_configuration"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ContainerRecommendation:
    out: ContainerRecommendation = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    if "memorySizeConfiguration" in data:
        import aws_sdk_compute_optimizer.types.memory_size_configuration

        out["memory_size_configuration"] = (
            aws_sdk_compute_optimizer.types.memory_size_configuration.deserialize_aws_json_1_0(
                data["memorySizeConfiguration"]
            )
        )
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    return out
