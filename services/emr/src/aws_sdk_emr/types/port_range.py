"""Generated from Smithy shape ``com.amazonaws.emr#PortRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.port


class PortRange(TypedDict):
    min_range: NotRequired["aws_sdk_emr.types.port.Port"]
    """<p>The smallest port number in a specified range of port numbers.</p>"""
    max_range: NotRequired["aws_sdk_emr.types.port.Port"]
    """<p>The smallest port number in a specified range of port numbers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortRange) -> dict:
    out: dict = {}
    if "min_range" in value:
        out["MinRange"] = value["min_range"]
    if "max_range" in value:
        out["MaxRange"] = value["max_range"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    if "MinRange" in data:
        out["min_range"] = data["MinRange"]
    if "MaxRange" in data:
        out["max_range"] = data["MaxRange"]
    return out
