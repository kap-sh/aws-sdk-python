"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EksResourceScalingUngraceful``."""

from typing_extensions import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError


class EksResourceScalingUngraceful(TypedDict, closed=True):
    minimum_success_percentage: "int"
    """<p>The minimum success percentage for the configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EksResourceScalingUngraceful) -> dict:
    out: dict = {}
    out["minimumSuccessPercentage"] = value["minimum_success_percentage"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EksResourceScalingUngraceful:
    out: EksResourceScalingUngraceful = {}  # type: ignore[typeddict-item]
    if "minimumSuccessPercentage" in data:
        out["minimum_success_percentage"] = data["minimumSuccessPercentage"]
    else:
        raise DeserializationError(
            "EksResourceScalingUngraceful.minimum_success_percentage required"
        )
    return out
