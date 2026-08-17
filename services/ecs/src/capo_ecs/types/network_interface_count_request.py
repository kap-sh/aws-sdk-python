"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkInterfaceCountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer


class NetworkInterfaceCountRequest(TypedDict, closed=True):
    min: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The minimum number of network interfaces. Instance types that support fewer network interfaces are excluded from selection.</p>"""
    max: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of network interfaces. Instance types that support more network interfaces are excluded from selection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterfaceCountRequest) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkInterfaceCountRequest:
    out: NetworkInterfaceCountRequest = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = data["min"]
    if data.get("max") is not None:
        out["max"] = data["max"]
    return out
