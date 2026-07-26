"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseQueryValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.quick_response_query_value

QuickResponseQueryValueList: TypeAlias = list[
    "capo_qconnect.types.quick_response_query_value.QuickResponseQueryValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseQueryValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> QuickResponseQueryValueList:
    return list(data)
