"""Generated from Smithy shape ``com.amazonaws.batch#RuntimePlatform``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class RuntimePlatform(TypedDict, closed=True):
    operating_system_family: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The operating system for the compute environment. Valid values are: <code>LINUX</code> (default), <code>WINDOWS_SERVER_2019_CORE</code>, <code>WINDOWS_SERVER_2019_FULL</code>, <code>WINDOWS_SERVER_2022_CORE</code>, and <code>WINDOWS_SERVER_2022_FULL</code>.</p> <note> <p>The following parameters can’t be set for Windows containers: <code>linuxParameters</code>, <code>privileged</code>, <code>user</code>, <code>ulimits</code>, <code>readonlyRootFilesystem</code>, and <code>efsVolumeConfiguration</code>.</p> </note> <note> <p>The Batch Scheduler checks the compute environments that are attached to the job queue before registering a task definition with Fargate. In this scenario, the job queue is where the job is submitted. If the job requires a Windows container and the first compute environment is <code>LINUX</code>, the compute environment is skipped and the next compute environment is checked until a Windows-based compute environment is found.</p> </note> <note> <p>Fargate Spot is not supported on Windows-based containers on Fargate. A job queue will be blocked if a Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both <code>FARGATE</code> and <code>FARGATE_SPOT</code> compute environments to the same job queue.</p> </note>"""
    cpu_architecture: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The vCPU architecture. The default value is <code>X86_64</code>. Valid values are <code>X86_64</code> and <code>ARM64</code>.</p> <note> <p>This parameter must be set to <code>X86_64</code> for Windows containers.</p> </note> <note> <p>Fargate Spot is not supported on Windows-based containers on Fargate. A job queue will be blocked if a Windows job is submitted to a job queue with only Fargate Spot compute environments. However, you can attach both <code>FARGATE</code> and <code>FARGATE_SPOT</code> compute environments to the same job queue.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimePlatform) -> dict:
    out: dict = {}
    if "operating_system_family" in value:
        out["operatingSystemFamily"] = value["operating_system_family"]
    if "cpu_architecture" in value:
        out["cpuArchitecture"] = value["cpu_architecture"]
    return out


def deserialize_json(data: dict) -> RuntimePlatform:
    out: RuntimePlatform = {}  # type: ignore[typeddict-item]
    if "operatingSystemFamily" in data:
        out["operating_system_family"] = data["operatingSystemFamily"]
    if "cpuArchitecture" in data:
        out["cpu_architecture"] = data["cpuArchitecture"]
    return out
