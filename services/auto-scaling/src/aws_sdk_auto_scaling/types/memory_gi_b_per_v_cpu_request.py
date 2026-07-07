"""Generated from Smithy shape ``com.amazonaws.autoscaling#MemoryGiBPerVCpuRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.nullable_positive_double


class MemoryGiBPerVCpuRequest(TypedDict, closed=True):
    min: NotRequired[
        "aws_sdk_auto_scaling.types.nullable_positive_double.NullablePositiveDouble"
    ]
    """<p>The memory minimum in GiB.</p>"""
    max: NotRequired[
        "aws_sdk_auto_scaling.types.nullable_positive_double.NullablePositiveDouble"
    ]
    """<p>The memory maximum in GiB.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MemoryGiBPerVCpuRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min" in value:
        pairs.append((f"{prefix}.Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{prefix}.Max", str(value["max"])))


def deserialize_query(el: Element) -> MemoryGiBPerVCpuRequest:
    out: MemoryGiBPerVCpuRequest = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = float(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = float(child_max.text or "")
    return out
