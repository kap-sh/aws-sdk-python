"""Generated from Smithy shape ``com.amazonaws.wafv2#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.conditions
    import aws_sdk_wafv2.types.filter_behavior
    import aws_sdk_wafv2.types.filter_requirement


class Filter(TypedDict, closed=True):
    behavior: "aws_sdk_wafv2.types.filter_behavior.FilterBehavior"
    """<p>How to handle logs that satisfy the filter's conditions and requirement. </p>"""
    requirement: "aws_sdk_wafv2.types.filter_requirement.FilterRequirement"
    """<p>Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.</p>"""
    conditions: "aws_sdk_wafv2.types.conditions.Conditions"
    """<p>Match conditions for the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    import aws_sdk_wafv2.types.filter_behavior

    out["Behavior"] = aws_sdk_wafv2.types.filter_behavior.serialize_aws_json_1_1(
        value["behavior"]
    )
    import aws_sdk_wafv2.types.filter_requirement

    out["Requirement"] = aws_sdk_wafv2.types.filter_requirement.serialize_aws_json_1_1(
        value["requirement"]
    )
    import aws_sdk_wafv2.types.conditions

    out["Conditions"] = aws_sdk_wafv2.types.conditions.serialize_aws_json_1_1(
        value["conditions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Behavior" in data:
        import aws_sdk_wafv2.types.filter_behavior

        out["behavior"] = aws_sdk_wafv2.types.filter_behavior.deserialize_aws_json_1_1(
            data["Behavior"]
        )
    else:
        raise DeserializationError("Filter.behavior required")
    if "Requirement" in data:
        import aws_sdk_wafv2.types.filter_requirement

        out["requirement"] = (
            aws_sdk_wafv2.types.filter_requirement.deserialize_aws_json_1_1(
                data["Requirement"]
            )
        )
    else:
        raise DeserializationError("Filter.requirement required")
    if "Conditions" in data:
        import aws_sdk_wafv2.types.conditions

        out["conditions"] = aws_sdk_wafv2.types.conditions.deserialize_aws_json_1_1(
            data["Conditions"]
        )
    else:
        raise DeserializationError("Filter.conditions required")
    return out
