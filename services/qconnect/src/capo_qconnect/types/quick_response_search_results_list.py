"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseSearchResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.quick_response_search_result_data

QuickResponseSearchResultsList: TypeAlias = list[
    "capo_qconnect.types.quick_response_search_result_data.QuickResponseSearchResultData"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseSearchResultsList) -> list:
    import capo_qconnect.types.quick_response_search_result_data

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.quick_response_search_result_data.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> QuickResponseSearchResultsList:
    import capo_qconnect.types.quick_response_search_result_data

    out: QuickResponseSearchResultsList = []
    for item in data:
        out.append(
            capo_qconnect.types.quick_response_search_result_data.deserialize_json(item)
        )
    return out
