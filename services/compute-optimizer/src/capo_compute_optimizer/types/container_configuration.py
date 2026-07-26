"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ContainerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.container_name
    import capo_compute_optimizer.types.memory_size_configuration
    import capo_compute_optimizer.types.nullable_cpu


class ContainerConfiguration(TypedDict, closed=True):
    container_name: NotRequired[
        "capo_compute_optimizer.types.container_name.ContainerName"
    ]
    """<p> The name of the container. </p>"""
    memory_size_configuration: NotRequired[
        "capo_compute_optimizer.types.memory_size_configuration.MemorySizeConfiguration"
    ]
    """<p> The memory size configurations for the container. </p>"""
    cpu: NotRequired["capo_compute_optimizer.types.nullable_cpu.NullableCpu"]
    """<p> The number of CPU units reserved for the container. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContainerConfiguration) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "memory_size_configuration" in value:
        import capo_compute_optimizer.types.memory_size_configuration

        out["memorySizeConfiguration"] = (
            capo_compute_optimizer.types.memory_size_configuration.serialize_aws_json_1_0(
                value["memory_size_configuration"]
            )
        )
    if "cpu" in value:
        out["cpu"] = value["cpu"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ContainerConfiguration:
    out: ContainerConfiguration = {}  # type: ignore[typeddict-item]
    if "containerName" in data:
        out["container_name"] = data["containerName"]
    if "memorySizeConfiguration" in data:
        import capo_compute_optimizer.types.memory_size_configuration

        out["memory_size_configuration"] = (
            capo_compute_optimizer.types.memory_size_configuration.deserialize_aws_json_1_0(
                data["memorySizeConfiguration"]
            )
        )
    if "cpu" in data:
        out["cpu"] = data["cpu"]
    return out
