"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUnameSuccessResponseItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.batch_uname_success_response_item

BatchUnameSuccessResponseItems: TypeAlias = list[
    "capo_wickr.types.batch_uname_success_response_item.BatchUnameSuccessResponseItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUnameSuccessResponseItems) -> list:
    import capo_wickr.types.batch_uname_success_response_item

    out: list = []
    for item in value:
        out.append(
            capo_wickr.types.batch_uname_success_response_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchUnameSuccessResponseItems:
    import capo_wickr.types.batch_uname_success_response_item

    out: BatchUnameSuccessResponseItems = []
    for item in data:
        out.append(
            capo_wickr.types.batch_uname_success_response_item.deserialize_json(item)
        )
    return out
