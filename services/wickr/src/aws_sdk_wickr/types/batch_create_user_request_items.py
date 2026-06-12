"""Generated from Smithy shape ``com.amazonaws.wickr#BatchCreateUserRequestItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wickr.types.batch_create_user_request_item

BatchCreateUserRequestItems: TypeAlias = list[
    "aws_sdk_wickr.types.batch_create_user_request_item.BatchCreateUserRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateUserRequestItems) -> list:
    import aws_sdk_wickr.types.batch_create_user_request_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wickr.types.batch_create_user_request_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BatchCreateUserRequestItems:
    import aws_sdk_wickr.types.batch_create_user_request_item

    out: BatchCreateUserRequestItems = []
    for item in data:
        out.append(
            aws_sdk_wickr.types.batch_create_user_request_item.deserialize_json(item)
        )
    return out
