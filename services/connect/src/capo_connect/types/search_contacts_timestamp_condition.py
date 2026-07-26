"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsTimestampCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_time_range_condition_type
    import capo_connect.types.search_contacts_time_range_type


class SearchContactsTimestampCondition(TypedDict, closed=True):
    type: (
        "capo_connect.types.search_contacts_time_range_type.SearchContactsTimeRangeType"
    )
    """<p>Type of the timestamps to use for the filter.</p>"""
    condition_type: "capo_connect.types.search_contacts_time_range_condition_type.SearchContactsTimeRangeConditionType"
    """<p>Condition of the timestamp on the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsTimestampCondition) -> dict:
    out: dict = {}
    import capo_connect.types.search_contacts_time_range_type

    out["Type"] = capo_connect.types.search_contacts_time_range_type.serialize_json(
        value["type"]
    )
    import capo_connect.types.search_contacts_time_range_condition_type

    out["ConditionType"] = (
        capo_connect.types.search_contacts_time_range_condition_type.serialize_json(
            value["condition_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchContactsTimestampCondition:
    out: SearchContactsTimestampCondition = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_connect.types.search_contacts_time_range_type

        out["type"] = (
            capo_connect.types.search_contacts_time_range_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("SearchContactsTimestampCondition.type required")
    if "ConditionType" in data:
        import capo_connect.types.search_contacts_time_range_condition_type

        out["condition_type"] = (
            capo_connect.types.search_contacts_time_range_condition_type.deserialize_json(
                data["ConditionType"]
            )
        )
    else:
        raise DeserializationError(
            "SearchContactsTimestampCondition.condition_type required"
        )
    return out
