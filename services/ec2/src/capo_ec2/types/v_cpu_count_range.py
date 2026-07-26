"""Generated from Smithy shape ``com.amazonaws.ec2#VCpuCountRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer


class VCpuCountRange(TypedDict, closed=True):
    min: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The minimum number of vCPUs. If the value is <code>0</code>, there is no minimum limit.</p>"""
    max: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of vCPUs. If this parameter is not specified, there is no maximum limit.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VCpuCountRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min" in value:
        pairs.append((f"{prefix}.Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{prefix}.Max", str(value["max"])))


def deserialize_ec2_query(el: Element) -> VCpuCountRange:
    out: VCpuCountRange = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = int(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = int(child_max.text or "")
    return out
