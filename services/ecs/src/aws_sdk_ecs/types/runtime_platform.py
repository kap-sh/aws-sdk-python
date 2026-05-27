"""Generated from Smithy shape ``com.amazonaws.ecs#RuntimePlatform``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.cpu_architecture
    import aws_sdk_ecs.types.os_family


class RuntimePlatform(TypedDict):
    cpu_architecture: NotRequired["aws_sdk_ecs.types.cpu_architecture.CPUArchitecture"]
    """<p>The CPU architecture.</p> <p>You can run your Linux tasks on an ARM-based platform by setting the value to <code>ARM64</code>. This option is available for tasks that run on Linux Amazon EC2 instance, Amazon ECS Managed Instances, or Linux containers on Fargate.</p>"""
    operating_system_family: NotRequired["aws_sdk_ecs.types.os_family.OSFamily"]
    """<p>The operating system.</p>"""
