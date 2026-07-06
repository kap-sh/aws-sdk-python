"""Generated from Smithy shape ``com.amazonaws.connect#ControlPlaneTagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.tag_and_condition_list
    import aws_sdk_connect.types.tag_condition
    import aws_sdk_connect.types.tag_or_condition_list


class ControlPlaneTagFilter(TypedDict, closed=True):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.tag_or_condition_list.TagOrConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_conditions: NotRequired[
        "aws_sdk_connect.types.tag_and_condition_list.TagAndConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    tag_condition: NotRequired["aws_sdk_connect.types.tag_condition.TagCondition"]
    """<p>A leaf node condition which can be used to specify a tag condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneTagFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.tag_or_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.tag_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import aws_sdk_connect.types.tag_and_condition_list

        out["AndConditions"] = (
            aws_sdk_connect.types.tag_and_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "tag_condition" in value:
        import aws_sdk_connect.types.tag_condition

        out["TagCondition"] = aws_sdk_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    return out


def deserialize_json(data: dict) -> ControlPlaneTagFilter:
    out: ControlPlaneTagFilter = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.tag_or_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.tag_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import aws_sdk_connect.types.tag_and_condition_list

        out["and_conditions"] = (
            aws_sdk_connect.types.tag_and_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "TagCondition" in data:
        import aws_sdk_connect.types.tag_condition

        out["tag_condition"] = aws_sdk_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    return out
