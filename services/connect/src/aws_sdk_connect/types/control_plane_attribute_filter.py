"""Generated from Smithy shape ``com.amazonaws.connect#ControlPlaneAttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.common_attribute_and_condition
    import aws_sdk_connect.types.common_attribute_or_condition_list
    import aws_sdk_connect.types.tag_condition


class ControlPlaneAttributeFilter(TypedDict, closed=True):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.common_attribute_or_condition_list.CommonAttributeOrConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_condition: NotRequired[
        "aws_sdk_connect.types.common_attribute_and_condition.CommonAttributeAndCondition"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    tag_condition: NotRequired["aws_sdk_connect.types.tag_condition.TagCondition"]


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneAttributeFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.common_attribute_or_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.common_attribute_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_condition" in value:
        import aws_sdk_connect.types.common_attribute_and_condition

        out["AndCondition"] = (
            aws_sdk_connect.types.common_attribute_and_condition.serialize_json(
                value["and_condition"]
            )
        )
    if "tag_condition" in value:
        import aws_sdk_connect.types.tag_condition

        out["TagCondition"] = aws_sdk_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    return out


def deserialize_json(data: dict) -> ControlPlaneAttributeFilter:
    out: ControlPlaneAttributeFilter = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.common_attribute_or_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.common_attribute_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndCondition" in data:
        import aws_sdk_connect.types.common_attribute_and_condition

        out["and_condition"] = (
            aws_sdk_connect.types.common_attribute_and_condition.deserialize_json(
                data["AndCondition"]
            )
        )
    if "TagCondition" in data:
        import aws_sdk_connect.types.tag_condition

        out["tag_condition"] = aws_sdk_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    return out
