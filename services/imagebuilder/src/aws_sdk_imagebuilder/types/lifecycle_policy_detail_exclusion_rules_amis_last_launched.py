"""Generated from Smithy shape ``com.amazonaws.imagebuilder#LifecyclePolicyDetailExclusionRulesAmisLastLaunched``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched_value
    import aws_sdk_imagebuilder.types.lifecycle_policy_time_unit


class LifecyclePolicyDetailExclusionRulesAmisLastLaunched(TypedDict):
    value: "aws_sdk_imagebuilder.types.lifecycle_policy_detail_exclusion_rules_amis_last_launched_value.LifecyclePolicyDetailExclusionRulesAmisLastLaunchedValue"
    """<p>The integer number of units for the time period. For example <code>6</code> (months).</p>"""
    unit: (
        "aws_sdk_imagebuilder.types.lifecycle_policy_time_unit.LifecyclePolicyTimeUnit"
    )
    """<p>Defines the unit of time that the lifecycle policy uses to calculate elapsed time since the last instance launched from the AMI. For example: days, weeks, months, or years.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicyDetailExclusionRulesAmisLastLaunched) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    import aws_sdk_imagebuilder.types.lifecycle_policy_time_unit

    out["unit"] = aws_sdk_imagebuilder.types.lifecycle_policy_time_unit.serialize_json(
        value["unit"]
    )
    return out


def deserialize_json(data: dict) -> LifecyclePolicyDetailExclusionRulesAmisLastLaunched:
    out: LifecyclePolicyDetailExclusionRulesAmisLastLaunched = {}  # type: ignore[typeddict-item]
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError(
            "LifecyclePolicyDetailExclusionRulesAmisLastLaunched.value required"
        )
    if "unit" in data:
        import aws_sdk_imagebuilder.types.lifecycle_policy_time_unit

        out["unit"] = (
            aws_sdk_imagebuilder.types.lifecycle_policy_time_unit.deserialize_json(
                data["unit"]
            )
        )
    else:
        raise DeserializationError(
            "LifecyclePolicyDetailExclusionRulesAmisLastLaunched.unit required"
        )
    return out
