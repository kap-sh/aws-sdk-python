"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUserSuccessResponseItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.batch_user_success_response_item

BatchUserSuccessResponseItems: TypeAlias = list[
    "capo_wickr.types.batch_user_success_response_item.BatchUserSuccessResponseItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUserSuccessResponseItems) -> list:
    import capo_wickr.types.batch_user_success_response_item

    out: list = []
    for item in value:
        out.append(
            capo_wickr.types.batch_user_success_response_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchUserSuccessResponseItems:
    import capo_wickr.types.batch_user_success_response_item

    out: BatchUserSuccessResponseItems = []
    for item in data:
        out.append(
            capo_wickr.types.batch_user_success_response_item.deserialize_json(item)
        )
    return out
