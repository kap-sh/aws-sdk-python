"""Generated from Smithy shape ``com.amazonaws.ec2#TotalLocalStorageGB``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.double


class TotalLocalStorageGB(TypedDict, closed=True):
    min: NotRequired["capo_ec2.types.double.Double"]
    """<p>The minimum amount of total local storage, in GB. If this parameter is not specified, there is no minimum limit.</p>"""
    max: NotRequired["capo_ec2.types.double.Double"]
    """<p>The maximum amount of total local storage, in GB. If this parameter is not specified, there is no maximum limit.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TotalLocalStorageGB, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min" in value:
        pairs.append((f"{key_prefix}Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{key_prefix}Max", str(value["max"])))


def deserialize_ec2_query(el: Element) -> TotalLocalStorageGB:
    out: TotalLocalStorageGB = {}  # type: ignore[typeddict-item]
    child_min = el.find("min")
    if child_min is not None:
        out["min"] = float(child_min.text or "")
    child_max = el.find("max")
    if child_max is not None:
        out["max"] = float(child_max.text or "")
    return out
