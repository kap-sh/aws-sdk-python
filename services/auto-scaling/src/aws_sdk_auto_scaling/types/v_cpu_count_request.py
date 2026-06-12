"""Generated from Smithy shape ``com.amazonaws.autoscaling#VCpuCountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.nullable_positive_integer


class VCpuCountRequest(TypedDict):
    min: NotRequired[
        "aws_sdk_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>The minimum number of vCPUs.</p>"""
    max: NotRequired[
        "aws_sdk_auto_scaling.types.nullable_positive_integer.NullablePositiveInteger"
    ]
    """<p>The maximum number of vCPUs.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VCpuCountRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "min" in value:
        pairs.append((f"{prefix}.Min", str(value["min"])))
    if "max" in value:
        pairs.append((f"{prefix}.Max", str(value["max"])))


def deserialize_query(el: Element) -> VCpuCountRequest:
    out: VCpuCountRequest = {}  # type: ignore[typeddict-item]
    child_min = el.find("Min")
    if child_min is not None:
        out["min"] = int(child_min.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = int(child_max.text or "")
    return out
