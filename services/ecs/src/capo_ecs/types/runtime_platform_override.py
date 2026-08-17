"""Generated from Smithy shape ``com.amazonaws.ecs#RuntimePlatformOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class RuntimePlatformOverride(TypedDict, closed=True):
    cpu_architecture: NotRequired["capo_ecs.types.string.String"]
    """<p>The CPU architecture that tasks in this service revision run on. This value might differ from the architecture declared in the task definition—for example, when Amazon ECS detects an architecture mismatch during an Amazon ECS Express deployment and runs tasks on a different architecture. You can't set this value.</p> <p>Valid values:</p> <ul> <li> <p> <code>X86_64</code> - The x86 64-bit architecture.</p> </li> <li> <p> <code>ARM64</code> - The 64-bit ARM architecture.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuntimePlatformOverride) -> dict:
    out: dict = {}
    if "cpu_architecture" in value:
        out["cpuArchitecture"] = value["cpu_architecture"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuntimePlatformOverride:
    out: RuntimePlatformOverride = {}  # type: ignore[typeddict-item]
    if data.get("cpuArchitecture") is not None:
        out["cpu_architecture"] = data["cpuArchitecture"]
    return out
