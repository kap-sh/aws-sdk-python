"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#PutVoiceConnectorExternalSystemsConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.contact_center_system_type_list
    import capo_chime_sdk_voice.types.non_empty_string128
    import capo_chime_sdk_voice.types.session_border_controller_type_list


class PutVoiceConnectorExternalSystemsConfigurationRequest(TypedDict, closed=True):
    voice_connector_id: (
        "capo_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The ID of the Voice Connector for which to add the external system configuration.</p>"""
    session_border_controller_types: NotRequired[
        "capo_chime_sdk_voice.types.session_border_controller_type_list.SessionBorderControllerTypeList"
    ]
    """<p>The session border controllers to use.</p>"""
    contact_center_system_types: NotRequired[
        "capo_chime_sdk_voice.types.contact_center_system_type_list.ContactCenterSystemTypeList"
    ]
    """<p>The contact center system to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutVoiceConnectorExternalSystemsConfigurationRequest) -> dict:
    out: dict = {}
    if "session_border_controller_types" in value:
        import capo_chime_sdk_voice.types.session_border_controller_type_list

        out["SessionBorderControllerTypes"] = (
            capo_chime_sdk_voice.types.session_border_controller_type_list.serialize_json(
                value["session_border_controller_types"]
            )
        )
    if "contact_center_system_types" in value:
        import capo_chime_sdk_voice.types.contact_center_system_type_list

        out["ContactCenterSystemTypes"] = (
            capo_chime_sdk_voice.types.contact_center_system_type_list.serialize_json(
                value["contact_center_system_types"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> PutVoiceConnectorExternalSystemsConfigurationRequest:
    out: PutVoiceConnectorExternalSystemsConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "SessionBorderControllerTypes" in data:
        import capo_chime_sdk_voice.types.session_border_controller_type_list

        out["session_border_controller_types"] = (
            capo_chime_sdk_voice.types.session_border_controller_type_list.deserialize_json(
                data["SessionBorderControllerTypes"]
            )
        )
    if "ContactCenterSystemTypes" in data:
        import capo_chime_sdk_voice.types.contact_center_system_type_list

        out["contact_center_system_types"] = (
            capo_chime_sdk_voice.types.contact_center_system_type_list.deserialize_json(
                data["ContactCenterSystemTypes"]
            )
        )
    return out
