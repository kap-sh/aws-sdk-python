"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileSearchCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.routing_profile_search_condition_list
    import aws_sdk_connect.types.string_condition


class RoutingProfileSearchCriteria(TypedDict):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.routing_profile_search_condition_list.RoutingProfileSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an OR condition.</p>"""
    and_conditions: NotRequired[
        "aws_sdk_connect.types.routing_profile_search_condition_list.RoutingProfileSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an AND condition.</p>"""
    string_condition: NotRequired[
        "aws_sdk_connect.types.string_condition.StringCondition"
    ]
    """<p>A leaf node condition which can be used to specify a string condition.</p> <note> <p>The currently supported values for <code>FieldName</code> are <code>associatedQueueIds</code>, <code>name</code>, <code>description</code>, and <code>resourceID</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.routing_profile_search_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.routing_profile_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import aws_sdk_connect.types.routing_profile_search_condition_list

        out["AndConditions"] = (
            aws_sdk_connect.types.routing_profile_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import aws_sdk_connect.types.string_condition

        out["StringCondition"] = aws_sdk_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    return out


def deserialize_json(data: dict) -> RoutingProfileSearchCriteria:
    out: RoutingProfileSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.routing_profile_search_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.routing_profile_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import aws_sdk_connect.types.routing_profile_search_condition_list

        out["and_conditions"] = (
            aws_sdk_connect.types.routing_profile_search_condition_list.deserialize_json(
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
    return out
