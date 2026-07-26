"""Generated from Smithy shape ``com.amazonaws.connectcases#SearchCasesResponseItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.search_cases_response_item

SearchCasesResponseItemList: TypeAlias = list[
    "capo_connectcases.types.search_cases_response_item.SearchCasesResponseItem | None"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchCasesResponseItemList) -> list:
    import capo_connectcases.types.search_cases_response_item

    out: list = []
    for item in value:
        if item is None:
            out.append(None)
            continue
        out.append(
            capo_connectcases.types.search_cases_response_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchCasesResponseItemList:
    import capo_connectcases.types.search_cases_response_item

    out: SearchCasesResponseItemList = []
    for item in data:
        if item is None:
            out.append(None)
            continue
        out.append(
            capo_connectcases.types.search_cases_response_item.deserialize_json(item)
        )
    return out
