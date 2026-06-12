"""Generated from Smithy shape ``com.amazonaws.connect#NotificationContent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.locale_code
    import aws_sdk_connect.types.localized_string

NotificationContent: TypeAlias = dict[
    "aws_sdk_connect.types.locale_code.LocaleCode",
    "aws_sdk_connect.types.localized_string.LocalizedString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: NotificationContent) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect.types.locale_code

        out[aws_sdk_connect.types.locale_code.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> NotificationContent:
    out: NotificationContent = {}
    for key, value in data.items():
        import aws_sdk_connect.types.locale_code

        out[aws_sdk_connect.types.locale_code.deserialize_json(key)] = value
    return out
