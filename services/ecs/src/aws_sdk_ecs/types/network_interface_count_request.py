"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkInterfaceCountRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer


class NetworkInterfaceCountRequest(TypedDict):
    min: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The minimum number of network interfaces. Instance types that support fewer network interfaces are excluded from selection.</p>"""
    max: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
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
    if "min" in data:
        out["min"] = data["min"]
    if "max" in data:
        out["max"] = data["max"]
    return out
