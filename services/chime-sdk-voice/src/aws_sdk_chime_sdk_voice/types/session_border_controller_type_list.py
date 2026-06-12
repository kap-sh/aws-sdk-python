"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SessionBorderControllerTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.session_border_controller_type

SessionBorderControllerTypeList: TypeAlias = list[
    "aws_sdk_chime_sdk_voice.types.session_border_controller_type.SessionBorderControllerType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionBorderControllerTypeList) -> list:
    import aws_sdk_chime_sdk_voice.types.session_border_controller_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_voice.types.session_border_controller_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SessionBorderControllerTypeList:
    import aws_sdk_chime_sdk_voice.types.session_border_controller_type

    out: SessionBorderControllerTypeList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_voice.types.session_border_controller_type.deserialize_json(
                item
            )
        )
    return out
