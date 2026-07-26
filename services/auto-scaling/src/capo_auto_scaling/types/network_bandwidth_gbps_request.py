"""Generated from Smithy shape ``com.amazonaws.autoscaling#NetworkBandwidthGbpsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.nullable_positive_double


class NetworkBandwidthGbpsRequest(TypedDict, closed=True):
    min: NotRequired[
        "capo_auto_scaling.types.nullable_positive_double.NullablePositiveDouble"
    ]
    """<p>The minimum amount of network bandwidth, in gigabits per second (Gbps).</p>"""
    max: NotRequired[
        "capo_auto_scaling.types.nullable_positive_double.NullablePositiveDouble"
    ]
    """<p>The maximum amount of network bandwidth, in gigabits per second (Gbps).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NetworkBandwidthGbpsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min" in value:
        pairs.append((f"{prefix}.Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{prefix}.Max", str(value["max"])))


def deserialize_query(el: Element) -> NetworkBandwidthGbpsRequest:
    out: NetworkBandwidthGbpsRequest = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = float(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = float(child_max.text or "")
    return out
