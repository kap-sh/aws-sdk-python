"""Generated from Smithy shape ``com.amazonaws.chime#UpdatePhoneNumberRequestItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime.types.update_phone_number_request_item

UpdatePhoneNumberRequestItemList: TypeAlias = list[
    "aws_sdk_chime.types.update_phone_number_request_item.UpdatePhoneNumberRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberRequestItemList) -> list:
    import aws_sdk_chime.types.update_phone_number_request_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime.types.update_phone_number_request_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UpdatePhoneNumberRequestItemList:
    import aws_sdk_chime.types.update_phone_number_request_item

    out: UpdatePhoneNumberRequestItemList = []
    for item in data:
        out.append(
            aws_sdk_chime.types.update_phone_number_request_item.deserialize_json(item)
        )
    return out
