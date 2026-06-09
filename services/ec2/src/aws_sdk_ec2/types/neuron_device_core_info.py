"""Generated from Smithy shape ``com.amazonaws.ec2#NeuronDeviceCoreInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.neuron_device_core_count
    import aws_sdk_ec2.types.neuron_device_core_version


class NeuronDeviceCoreInfo(TypedDict):
    count: NotRequired[
        "aws_sdk_ec2.types.neuron_device_core_count.NeuronDeviceCoreCount"
    ]
    """<p>The number of cores available to the neuron accelerator.</p>"""
    version: NotRequired[
        "aws_sdk_ec2.types.neuron_device_core_version.NeuronDeviceCoreVersion"
    ]
    """<p>The version of the neuron accelerator.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NeuronDeviceCoreInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "count" in value:
        pairs.append((f"{prefix}.Count", str(value["count"])))
    if "version" in value:
        pairs.append((f"{prefix}.Version", str(value["version"])))


def deserialize_ec2_query(el: Element) -> NeuronDeviceCoreInfo:
    out: NeuronDeviceCoreInfo = {}  # type: ignore[typeddict-item]
    child_count = el.find("Count")
    if child_count is not None:
        out["count"] = int(child_count.text or "")
    child_version = el.find("Version")
    if child_version is not None:
        out["version"] = int(child_version.text or "")
    return out
