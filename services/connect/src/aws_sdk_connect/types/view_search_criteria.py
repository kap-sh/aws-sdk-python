"""Generated from Smithy shape ``com.amazonaws.connect#ViewSearchCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.string_condition
    import aws_sdk_connect.types.view_search_condition_list
    import aws_sdk_connect.types.view_status
    import aws_sdk_connect.types.view_type


class ViewSearchCriteria(TypedDict):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.view_search_condition_list.ViewSearchConditionList"
    ]
    """<p>A list of conditions to be met, where at least one condition must be satisfied.</p>"""
    and_conditions: NotRequired[
        "aws_sdk_connect.types.view_search_condition_list.ViewSearchConditionList"
    ]
    """<p>A list of conditions that must all be satisfied.</p>"""
    string_condition: NotRequired[
        "aws_sdk_connect.types.string_condition.StringCondition"
    ]
    view_type_condition: NotRequired["aws_sdk_connect.types.view_type.ViewType"]
    """<p>A condition that filters views by their type.</p>"""
    view_status_condition: NotRequired["aws_sdk_connect.types.view_status.ViewStatus"]
    """<p>A condition that filters views by their status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.view_search_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.view_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import aws_sdk_connect.types.view_search_condition_list

        out["AndConditions"] = (
            aws_sdk_connect.types.view_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import aws_sdk_connect.types.string_condition

        out["StringCondition"] = aws_sdk_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "view_type_condition" in value:
        import aws_sdk_connect.types.view_type

        out["ViewTypeCondition"] = aws_sdk_connect.types.view_type.serialize_json(
            value["view_type_condition"]
        )
    if "view_status_condition" in value:
        import aws_sdk_connect.types.view_status

        out["ViewStatusCondition"] = aws_sdk_connect.types.view_status.serialize_json(
            value["view_status_condition"]
        )
    return out


def deserialize_json(data: dict) -> ViewSearchCriteria:
    out: ViewSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.view_search_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.view_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import aws_sdk_connect.types.view_search_condition_list

        out["and_conditions"] = (
            aws_sdk_connect.types.view_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import aws_sdk_connect.types.string_condition

        out["string_condition"] = (
            aws_sdk_connect.types.string_condition.deserialize_json(
                data["StringCondition"]
            )
        )
    if "ViewTypeCondition" in data:
        import aws_sdk_connect.types.view_type

        out["view_type_condition"] = aws_sdk_connect.types.view_type.deserialize_json(
            data["ViewTypeCondition"]
        )
    if "ViewStatusCondition" in data:
        import aws_sdk_connect.types.view_status

        out["view_status_condition"] = (
            aws_sdk_connect.types.view_status.deserialize_json(
                data["ViewStatusCondition"]
            )
        )
    return out
