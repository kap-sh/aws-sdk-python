"""Generated from Smithy shape ``com.amazonaws.connect#QueueSearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.queue_search_condition_list
    import capo_connect.types.searchable_queue_type
    import capo_connect.types.string_condition


class QueueSearchCriteria(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.queue_search_condition_list.QueueSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an OR condition.</p>"""
    and_conditions: NotRequired[
        "capo_connect.types.queue_search_condition_list.QueueSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an AND condition.</p>"""
    string_condition: NotRequired["capo_connect.types.string_condition.StringCondition"]
    """<p>A leaf node condition which can be used to specify a string condition.</p> <note> <p>The currently supported values for <code>FieldName</code> are <code>name</code>, <code>description</code>, and <code>resourceID</code>.</p> </note>"""
    queue_type_condition: NotRequired[
        "capo_connect.types.searchable_queue_type.SearchableQueueType"
    ]
    """<p>The type of queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.queue_search_condition_list

        out["OrConditions"] = (
            capo_connect.types.queue_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import capo_connect.types.queue_search_condition_list

        out["AndConditions"] = (
            capo_connect.types.queue_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import capo_connect.types.string_condition

        out["StringCondition"] = capo_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "queue_type_condition" in value:
        import capo_connect.types.searchable_queue_type

        out["QueueTypeCondition"] = (
            capo_connect.types.searchable_queue_type.serialize_json(
                value["queue_type_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> QueueSearchCriteria:
    out: QueueSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import capo_connect.types.queue_search_condition_list

        out["or_conditions"] = (
            capo_connect.types.queue_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import capo_connect.types.queue_search_condition_list

        out["and_conditions"] = (
            capo_connect.types.queue_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import capo_connect.types.string_condition

        out["string_condition"] = capo_connect.types.string_condition.deserialize_json(
            data["StringCondition"]
        )
    if "QueueTypeCondition" in data:
        import capo_connect.types.searchable_queue_type

        out["queue_type_condition"] = (
            capo_connect.types.searchable_queue_type.deserialize_json(
                data["QueueTypeCondition"]
            )
        )
    return out
