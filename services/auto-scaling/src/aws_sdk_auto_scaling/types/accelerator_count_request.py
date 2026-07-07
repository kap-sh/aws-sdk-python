"""Generated from Smithy shape ``com.amazonaws.autoscaling#AcceleratorCountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.nullable_positive_integer


class AcceleratorCountRequest(TypedDict, closed=True):
    min: NotRequired[
        "aws_sdk_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>The minimum value.</p>"""
    max: NotRequired[
        "aws_sdk_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>The maximum value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AcceleratorCountRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min" in value:
        pairs.append((f"{prefix}.Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{prefix}.Max", str(value["max"])))


def deserialize_query(el: Element) -> AcceleratorCountRequest:
    out: AcceleratorCountRequest = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = int(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = int(child_max.text or "")
    return out
