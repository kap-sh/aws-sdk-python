"""Generated from Smithy shape ``com.amazonaws.ecs#RuntimePlatform``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.cpu_architecture
    import capo_ecs.types.os_family


class RuntimePlatform(TypedDict, closed=True):
    cpu_architecture: NotRequired["capo_ecs.types.cpu_architecture.CPUArchitecture"]
    """<p>The CPU architecture.</p> <p>You can run your Linux tasks on an ARM-based platform by setting the value to <code>ARM64</code>. This option is available for tasks that run on Linux Amazon EC2 instance, Amazon ECS Managed Instances, or Linux containers on Fargate.</p>"""
    operating_system_family: NotRequired["capo_ecs.types.os_family.OSFamily"]
    """<p>The operating system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuntimePlatform) -> dict:
    out: dict = {}
    if "cpu_architecture" in value:
        import capo_ecs.types.cpu_architecture

        out["cpuArchitecture"] = capo_ecs.types.cpu_architecture.serialize_aws_json_1_1(
            value["cpu_architecture"]
        )
    if "operating_system_family" in value:
        import capo_ecs.types.os_family

        out["operatingSystemFamily"] = capo_ecs.types.os_family.serialize_aws_json_1_1(
            value["operating_system_family"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuntimePlatform:
    out: RuntimePlatform = {}  # type: ignore[typeddict-item]
    if "cpuArchitecture" in data:
        import capo_ecs.types.cpu_architecture

        out["cpu_architecture"] = (
            capo_ecs.types.cpu_architecture.deserialize_aws_json_1_1(
                data["cpuArchitecture"]
            )
        )
    if "operatingSystemFamily" in data:
        import capo_ecs.types.os_family

        out["operating_system_family"] = (
            capo_ecs.types.os_family.deserialize_aws_json_1_1(
                data["operatingSystemFamily"]
            )
        )
    return out
