"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ExternalSystemsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.contact_center_system_type_list
    import aws_sdk_chime_sdk_voice.types.session_border_controller_type_list


class ExternalSystemsConfiguration(TypedDict):
    session_border_controller_types: NotRequired[
        "aws_sdk_chime_sdk_voice.types.session_border_controller_type_list.SessionBorderControllerTypeList"
    ]
    """<p>The session border controllers.</p>"""
    contact_center_system_types: NotRequired[
        "aws_sdk_chime_sdk_voice.types.contact_center_system_type_list.ContactCenterSystemTypeList"
    ]
    """<p>The contact center system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSystemsConfiguration) -> dict:
    out: dict = {}
    if "session_border_controller_types" in value:
        import aws_sdk_chime_sdk_voice.types.session_border_controller_type_list

        out["SessionBorderControllerTypes"] = (
            aws_sdk_chime_sdk_voice.types.session_border_controller_type_list.serialize_json(
                value["session_border_controller_types"]
            )
        )
    if "contact_center_system_types" in value:
        import aws_sdk_chime_sdk_voice.types.contact_center_system_type_list

        out["ContactCenterSystemTypes"] = (
            aws_sdk_chime_sdk_voice.types.contact_center_system_type_list.serialize_json(
                value["contact_center_system_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExternalSystemsConfiguration:
    out: ExternalSystemsConfiguration = {}  # type: ignore[typeddict-item]
    if "SessionBorderControllerTypes" in data:
        import aws_sdk_chime_sdk_voice.types.session_border_controller_type_list

        out["session_border_controller_types"] = (
            aws_sdk_chime_sdk_voice.types.session_border_controller_type_list.deserialize_json(
                data["SessionBorderControllerTypes"]
            )
        )
    if "ContactCenterSystemTypes" in data:
        import aws_sdk_chime_sdk_voice.types.contact_center_system_type_list

        out["contact_center_system_types"] = (
            aws_sdk_chime_sdk_voice.types.contact_center_system_type_list.deserialize_json(
                data["ContactCenterSystemTypes"]
            )
        )
    return out
