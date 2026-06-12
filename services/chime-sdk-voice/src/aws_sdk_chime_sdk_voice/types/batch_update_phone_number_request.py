"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#BatchUpdatePhoneNumberRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.update_phone_number_request_item_list


class BatchUpdatePhoneNumberRequest(TypedDict):
    update_phone_number_request_items: "aws_sdk_chime_sdk_voice.types.update_phone_number_request_item_list.UpdatePhoneNumberRequestItemList"
    """<p>Lists the phone numbers in the update request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdatePhoneNumberRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_voice.types.update_phone_number_request_item_list

    out["UpdatePhoneNumberRequestItems"] = (
        aws_sdk_chime_sdk_voice.types.update_phone_number_request_item_list.serialize_json(
            value["update_phone_number_request_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdatePhoneNumberRequest:
    out: BatchUpdatePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if "UpdatePhoneNumberRequestItems" in data:
        import aws_sdk_chime_sdk_voice.types.update_phone_number_request_item_list

        out["update_phone_number_request_items"] = (
            aws_sdk_chime_sdk_voice.types.update_phone_number_request_item_list.deserialize_json(
                data["UpdatePhoneNumberRequestItems"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdatePhoneNumberRequest.update_phone_number_request_items required"
        )
    return out
