"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#BatchDeletePhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.non_empty_string_list


class BatchDeletePhoneNumberRequest(TypedDict, closed=True):
    phone_number_ids: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string_list.NonEmptyStringList"
    )
    """<p>List of phone number IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeletePhoneNumberRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_voice.types.non_empty_string_list

    out["PhoneNumberIds"] = (
        aws_sdk_chime_sdk_voice.types.non_empty_string_list.serialize_json(
            value["phone_number_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchDeletePhoneNumberRequest:
    out: BatchDeletePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if "PhoneNumberIds" in data:
        import aws_sdk_chime_sdk_voice.types.non_empty_string_list

        out["phone_number_ids"] = (
            aws_sdk_chime_sdk_voice.types.non_empty_string_list.deserialize_json(
                data["PhoneNumberIds"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeletePhoneNumberRequest.phone_number_ids required"
        )
    return out
