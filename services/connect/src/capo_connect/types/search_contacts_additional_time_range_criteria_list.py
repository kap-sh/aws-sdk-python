"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsAdditionalTimeRangeCriteriaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.search_contacts_additional_time_range_criteria

SearchContactsAdditionalTimeRangeCriteriaList: TypeAlias = list[
    "capo_connect.types.search_contacts_additional_time_range_criteria.SearchContactsAdditionalTimeRangeCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsAdditionalTimeRangeCriteriaList) -> list:
    import capo_connect.types.search_contacts_additional_time_range_criteria

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.search_contacts_additional_time_range_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SearchContactsAdditionalTimeRangeCriteriaList:
    import capo_connect.types.search_contacts_additional_time_range_criteria

    out: SearchContactsAdditionalTimeRangeCriteriaList = []
    for item in data:
        out.append(
            capo_connect.types.search_contacts_additional_time_range_criteria.deserialize_json(
                item
            )
        )
    return out
