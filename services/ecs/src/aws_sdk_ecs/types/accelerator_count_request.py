"""Generated from Smithy shape ``com.amazonaws.ecs#AcceleratorCountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class AcceleratorCountRequest(TypedDict, closed=True):
    min: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The minimum number of accelerators. Instance types with fewer accelerators are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of accelerators. Instance types with more accelerators are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceleratorCountRequest) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AcceleratorCountRequest:
    out: AcceleratorCountRequest = {}  # type: ignore[typeddict-item]
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    return out
