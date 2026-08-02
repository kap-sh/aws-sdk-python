"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorTotalMemoryMiBRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer


class AcceleratorTotalMemoryMiBRequest(TypedDict, closed=True):
    min: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The minimum amount of accelerator memory, in MiB. To specify no minimum limit, omit this parameter.</p>"""
    max: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum amount of accelerator memory, in MiB. To specify no maximum limit, omit this parameter.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceleratorTotalMemoryMiBRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min" in value:
        pairs.append((f"{key_prefix}Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{key_prefix}Max", str(value["max"])))


def deserialize_ec2_query(el: Element) -> AcceleratorTotalMemoryMiBRequest:
    out: AcceleratorTotalMemoryMiBRequest = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = int(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = int(child_max.text or "")
    return out
