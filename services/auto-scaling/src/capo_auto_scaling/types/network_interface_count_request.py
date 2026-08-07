"""Generated from Smithy shape ``com.amazonaws.autoscaling#NetworkInterfaceCountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.nullable_positive_integer


class NetworkInterfaceCountRequest(TypedDict, closed=True):
    min: NotRequired[
        "capo_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>The minimum number of network interfaces.</p>"""
    max: NotRequired[
        "capo_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>The maximum number of network interfaces.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NetworkInterfaceCountRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min" in value:
        pairs.append((f"{key_prefix}Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{key_prefix}Max", str(value["max"])))


def deserialize_query(el: Element) -> NetworkInterfaceCountRequest:
    out: NetworkInterfaceCountRequest = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = int(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = int(child_max.text or "")
    return out
