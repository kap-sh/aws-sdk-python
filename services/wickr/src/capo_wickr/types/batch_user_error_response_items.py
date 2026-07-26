"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUserErrorResponseItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.batch_user_error_response_item

BatchUserErrorResponseItems: TypeAlias = list[
    "capo_wickr.types.batch_user_error_response_item.BatchUserErrorResponseItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUserErrorResponseItems) -> list:
    import capo_wickr.types.batch_user_error_response_item

    out: list = []
    for item in value:
        out.append(capo_wickr.types.batch_user_error_response_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchUserErrorResponseItems:
    import capo_wickr.types.batch_user_error_response_item

    out: BatchUserErrorResponseItems = []
    for item in data:
        out.append(
            capo_wickr.types.batch_user_error_response_item.deserialize_json(item)
        )
    return out
