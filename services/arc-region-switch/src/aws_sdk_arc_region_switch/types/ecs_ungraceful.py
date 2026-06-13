"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EcsUngraceful``."""

from typing import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError


class EcsUngraceful(TypedDict):
    minimum_success_percentage: "int"
    """<p>The minimum success percentage specified for the configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EcsUngraceful) -> dict:
    out: dict = {}
    out["minimumSuccessPercentage"] = value["minimum_success_percentage"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EcsUngraceful:
    out: EcsUngraceful = {}  # type: ignore[typeddict-item]
    if "minimumSuccessPercentage" in data:
        out["minimum_success_percentage"] = data["minimumSuccessPercentage"]
    else:
        raise DeserializationError("EcsUngraceful.minimum_success_percentage required")
    return out
