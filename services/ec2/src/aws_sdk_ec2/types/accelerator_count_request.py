"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorCountRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class AcceleratorCountRequest(TypedDict):
    min: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The minimum number of accelerators. To specify no minimum limit, omit this parameter.</p>"""
    max: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The maximum number of accelerators. To specify no maximum limit, omit this parameter. To exclude accelerator-enabled instance types, set <code>Max</code> to <code>0</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceleratorCountRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min" in value:
        pairs.append((f"{prefix}.Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{prefix}.Max", str(value["max"])))


def deserialize_ec2_query(el: Element) -> AcceleratorCountRequest:
    out: AcceleratorCountRequest = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = int(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = int(child_max.text or "")
    return out
