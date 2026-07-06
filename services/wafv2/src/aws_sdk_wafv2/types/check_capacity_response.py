"""Generated from Smithy shape ``com.amazonaws.wafv2#CheckCapacityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.consumed_capacity


class CheckCapacityResponse(TypedDict, closed=True):
    capacity: "aws_sdk_wafv2.types.consumed_capacity.ConsumedCapacity"
    """<p>The capacity required by the rules and scope.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckCapacityResponse) -> dict:
    out: dict = {}
    out["Capacity"] = value.get("capacity", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckCapacityResponse:
    out: CheckCapacityResponse = {}  # type: ignore[typeddict-item]
    if "Capacity" in data:
        out["capacity"] = data["Capacity"]
    else:
        out["capacity"] = 0
    return out
