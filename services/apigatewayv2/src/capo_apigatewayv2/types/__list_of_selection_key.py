"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#__listOfSelectionKey``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apigatewayv2.types.selection_key

__listOfSelectionKey: TypeAlias = list[
    "capo_apigatewayv2.types.selection_key.SelectionKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSelectionKey) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOfSelectionKey:
    return list(data)
