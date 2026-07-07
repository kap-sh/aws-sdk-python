"""Generated from Smithy shape ``com.amazonaws.devicefarm#CPU``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.double
    import aws_sdk_device_farm.types.string


class CPU(TypedDict, closed=True):
    frequency: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>The CPU's frequency.</p>"""
    architecture: NotRequired["aws_sdk_device_farm.types.string.String"]
    """<p>The CPU's architecture (for example, x86 or ARM).</p>"""
    clock: NotRequired["aws_sdk_device_farm.types.double.Double"]
    """<p>The clock speed of the device's CPU, expressed in hertz (Hz). For example, a 1.2 GHz CPU is expressed as 1200000000.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CPU) -> dict:
    out: dict = {}
    if "frequency" in value:
        out["frequency"] = value["frequency"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "clock" in value:
        out["clock"] = value["clock"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CPU:
    out: CPU = {}  # type: ignore[typeddict-item]
    if "frequency" in data:
        out["frequency"] = data["frequency"]
    if "architecture" in data:
        out["architecture"] = data["architecture"]
    if "clock" in data:
        out["clock"] = data["clock"]
    return out
