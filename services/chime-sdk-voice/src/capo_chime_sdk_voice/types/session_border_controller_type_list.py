"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SessionBorderControllerTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.session_border_controller_type

SessionBorderControllerTypeList: TypeAlias = list[
    "capo_chime_sdk_voice.types.session_border_controller_type.SessionBorderControllerType"
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionBorderControllerTypeList) -> list:
    import capo_chime_sdk_voice.types.session_border_controller_type

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_voice.types.session_border_controller_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SessionBorderControllerTypeList:
    import capo_chime_sdk_voice.types.session_border_controller_type

    out: SessionBorderControllerTypeList = []
    for item in data:
        out.append(
            capo_chime_sdk_voice.types.session_border_controller_type.deserialize_json(
                item
            )
        )
    return out
