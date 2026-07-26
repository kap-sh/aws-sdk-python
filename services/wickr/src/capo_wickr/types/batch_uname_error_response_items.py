"""Generated from Smithy shape ``com.amazonaws.wickr#BatchUnameErrorResponseItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.batch_uname_error_response_item

BatchUnameErrorResponseItems: TypeAlias = list[
    "capo_wickr.types.batch_uname_error_response_item.BatchUnameErrorResponseItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUnameErrorResponseItems) -> list:
    import capo_wickr.types.batch_uname_error_response_item

    out: list = []
    for item in value:
        out.append(
            capo_wickr.types.batch_uname_error_response_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchUnameErrorResponseItems:
    import capo_wickr.types.batch_uname_error_response_item

    out: BatchUnameErrorResponseItems = []
    for item in data:
        out.append(
            capo_wickr.types.batch_uname_error_response_item.deserialize_json(item)
        )
    return out
