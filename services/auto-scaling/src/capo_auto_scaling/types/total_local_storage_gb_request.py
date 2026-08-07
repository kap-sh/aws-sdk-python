"""Generated from Smithy shape ``com.amazonaws.autoscaling#TotalLocalStorageGBRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.nullable_positive_double


class TotalLocalStorageGBRequest(TypedDict, closed=True):
    min: NotRequired[
        "capo_auto_scaling.types.nullable_positive_double.NullablePositiveDouble"
    ]
    """<p>The storage minimum in GB.</p>"""
    max: NotRequired[
        "capo_auto_scaling.types.nullable_positive_double.NullablePositiveDouble"
    ]
    """<p>The storage maximum in GB.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TotalLocalStorageGBRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "min" in value:
        pairs.append((f"{key_prefix}Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{key_prefix}Max", str(value["max"])))


def deserialize_query(el: Element) -> TotalLocalStorageGBRequest:
    out: TotalLocalStorageGBRequest = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = float(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = float(child_max.text or "")
    return out
