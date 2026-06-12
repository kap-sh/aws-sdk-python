"""Generated from Smithy shape ``com.amazonaws.gamelift#EC2InstanceCounts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.whole_number


class EC2InstanceCounts(TypedDict):
    desired: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>Requested number of active instances. Amazon GameLift Servers takes action as needed to maintain the desired number of instances. Capacity is scaled up or down by changing the desired instances. A change in the desired instances value can take up to 1 minute to be reflected when viewing a fleet's capacity settings. </p>"""
    minimum: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>The minimum instance count value allowed.</p>"""
    maximum: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>The maximum instance count value allowed.</p>"""
    pending: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>Number of instances that are starting but not yet active.</p>"""
    active: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>Actual number of instances that are ready to host game sessions.</p>"""
    idle: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>Number of active instances that are not currently hosting a game session.</p>"""
    terminating: NotRequired["aws_sdk_gamelift.types.whole_number.WholeNumber"]
    """<p>Number of instances that are no longer active but haven't yet been terminated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EC2InstanceCounts) -> dict:
    out: dict = {}
    if "desired" in value:
        out["DESIRED"] = value["desired"]
    if "minimum" in value:
        out["MINIMUM"] = value["minimum"]
    if "maximum" in value:
        out["MAXIMUM"] = value["maximum"]
    if "pending" in value:
        out["PENDING"] = value["pending"]
    if "active" in value:
        out["ACTIVE"] = value["active"]
    if "idle" in value:
        out["IDLE"] = value["idle"]
    if "terminating" in value:
        out["TERMINATING"] = value["terminating"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EC2InstanceCounts:
    out: EC2InstanceCounts = {}  # type: ignore[typeddict-item]
    if "DESIRED" in data:
        out["desired"] = data["DESIRED"]
    if "MINIMUM" in data:
        out["minimum"] = data["MINIMUM"]
    if "MAXIMUM" in data:
        out["maximum"] = data["MAXIMUM"]
    if "PENDING" in data:
        out["pending"] = data["PENDING"]
    if "ACTIVE" in data:
        out["active"] = data["ACTIVE"]
    if "IDLE" in data:
        out["idle"] = data["IDLE"]
    if "TERMINATING" in data:
        out["terminating"] = data["TERMINATING"]
    return out
