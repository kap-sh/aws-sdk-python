"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#DeleteKeyRequestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.delete_key_request_list_item

DeleteKeyRequestsList: TypeAlias = list[
    "capo_cloudfront_keyvaluestore.types.delete_key_request_list_item.DeleteKeyRequestListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKeyRequestsList) -> list:
    import capo_cloudfront_keyvaluestore.types.delete_key_request_list_item

    out: list = []
    for item in value:
        out.append(
            capo_cloudfront_keyvaluestore.types.delete_key_request_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DeleteKeyRequestsList:
    import capo_cloudfront_keyvaluestore.types.delete_key_request_list_item

    out: DeleteKeyRequestsList = []
    for item in data:
        out.append(
            capo_cloudfront_keyvaluestore.types.delete_key_request_list_item.deserialize_json(
                item
            )
        )
    return out
