"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsAdditionalTimeRangeCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_time_range
    import capo_connect.types.search_contacts_timestamp_condition


class SearchContactsAdditionalTimeRangeCriteria(TypedDict, closed=True):
    time_range: NotRequired[
        "capo_connect.types.search_contacts_time_range.SearchContactsTimeRange"
    ]
    timestamp_condition: NotRequired[
        "capo_connect.types.search_contacts_timestamp_condition.SearchContactsTimestampCondition"
    ]
    """<p>List of the timestamp conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsAdditionalTimeRangeCriteria) -> dict:
    out: dict = {}
    if "time_range" in value:
        import capo_connect.types.search_contacts_time_range

        out["TimeRange"] = capo_connect.types.search_contacts_time_range.serialize_json(
            value["time_range"]
        )
    if "timestamp_condition" in value:
        import capo_connect.types.search_contacts_timestamp_condition

        out["TimestampCondition"] = (
            capo_connect.types.search_contacts_timestamp_condition.serialize_json(
                value["timestamp_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchContactsAdditionalTimeRangeCriteria:
    out: SearchContactsAdditionalTimeRangeCriteria = {}  # type: ignore[typeddict-item]
    if "TimeRange" in data:
        import capo_connect.types.search_contacts_time_range

        out["time_range"] = (
            capo_connect.types.search_contacts_time_range.deserialize_json(
                data["TimeRange"]
            )
        )
    if "TimestampCondition" in data:
        import capo_connect.types.search_contacts_timestamp_condition

        out["timestamp_condition"] = (
            capo_connect.types.search_contacts_timestamp_condition.deserialize_json(
                data["TimestampCondition"]
            )
        )
    return out
