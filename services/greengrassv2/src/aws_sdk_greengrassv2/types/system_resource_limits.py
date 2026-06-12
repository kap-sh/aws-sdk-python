"""Generated from Smithy shape ``com.amazonaws.greengrassv2#SystemResourceLimits``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.cpu
    import aws_sdk_greengrassv2.types.memory


class SystemResourceLimits(TypedDict):
    memory: "aws_sdk_greengrassv2.types.memory.Memory"
    """<p>The maximum amount of RAM, expressed in kilobytes, that a component's processes can use on the core device.</p>"""
    cpus: "aws_sdk_greengrassv2.types.cpu.CPU"
    """<p>The maximum amount of CPU time that a component's processes can use on the core device. A core device's total CPU time is equivalent to the device's number of CPU cores. For example, on a core device with 4 CPU cores, you can set this value to <code>2</code> to limit the component's processes to 50 percent usage of each CPU core. On a device with 1 CPU core, you can set this value to <code>0.25</code> to limit the component's processes to 25 percent usage of the CPU. If you set this value to a number greater than the number of CPU cores, the IoT Greengrass Core software doesn't limit the component's CPU usage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemResourceLimits) -> dict:
    out: dict = {}
    out["memory"] = value.get("memory", 0)
    out["cpus"] = value.get("cpus", 0)
    return out


def deserialize_json(data: dict) -> SystemResourceLimits:
    out: SystemResourceLimits = {}  # type: ignore[typeddict-item]
    if "memory" in data:
        out["memory"] = data["memory"]
    else:
        out["memory"] = 0
    if "cpus" in data:
        out["cpus"] = data["cpus"]
    else:
        out["cpus"] = 0
    return out
