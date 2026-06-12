"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CreateProxySessionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_voice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.capability_list
    import aws_sdk_chime_sdk_voice.types.geo_match_level
    import aws_sdk_chime_sdk_voice.types.geo_match_params
    import aws_sdk_chime_sdk_voice.types.non_empty_string128
    import aws_sdk_chime_sdk_voice.types.number_selection_behavior
    import aws_sdk_chime_sdk_voice.types.participant_phone_number_list
    import aws_sdk_chime_sdk_voice.types.positive_integer
    import aws_sdk_chime_sdk_voice.types.proxy_session_name_string


class CreateProxySessionRequest(TypedDict):
    voice_connector_id: (
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    )
    """<p>The Voice Connector ID.</p>"""
    participant_phone_numbers: "aws_sdk_chime_sdk_voice.types.participant_phone_number_list.ParticipantPhoneNumberList"
    """<p>The participant phone numbers.</p>"""
    name: NotRequired[
        "aws_sdk_chime_sdk_voice.types.proxy_session_name_string.ProxySessionNameString"
    ]
    """<p>The name of the proxy session.</p>"""
    expiry_minutes: NotRequired[
        "aws_sdk_chime_sdk_voice.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of minutes allowed for the proxy session.</p>"""
    capabilities: "aws_sdk_chime_sdk_voice.types.capability_list.CapabilityList"
    """<p>The proxy session's capabilities.</p>"""
    number_selection_behavior: NotRequired[
        "aws_sdk_chime_sdk_voice.types.number_selection_behavior.NumberSelectionBehavior"
    ]
    """<p>The preference for proxy phone number reuse, or stickiness, between the same participants across sessions.</p>"""
    geo_match_level: NotRequired[
        "aws_sdk_chime_sdk_voice.types.geo_match_level.GeoMatchLevel"
    ]
    """<p>The preference for matching the country or area code of the proxy phone number with that of the first participant.</p>"""
    geo_match_params: NotRequired[
        "aws_sdk_chime_sdk_voice.types.geo_match_params.GeoMatchParams"
    ]
    """<p>The country and area code for the proxy phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProxySessionRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_voice.types.participant_phone_number_list

    out["ParticipantPhoneNumbers"] = (
        aws_sdk_chime_sdk_voice.types.participant_phone_number_list.serialize_json(
            value["participant_phone_numbers"]
        )
    )
    if "name" in value:
        out["Name"] = value["name"]
    if "expiry_minutes" in value:
        out["ExpiryMinutes"] = value["expiry_minutes"]
    import aws_sdk_chime_sdk_voice.types.capability_list

    out["Capabilities"] = aws_sdk_chime_sdk_voice.types.capability_list.serialize_json(
        value["capabilities"]
    )
    if "number_selection_behavior" in value:
        import aws_sdk_chime_sdk_voice.types.number_selection_behavior

        out["NumberSelectionBehavior"] = (
            aws_sdk_chime_sdk_voice.types.number_selection_behavior.serialize_json(
                value["number_selection_behavior"]
            )
        )
    if "geo_match_level" in value:
        import aws_sdk_chime_sdk_voice.types.geo_match_level

        out["GeoMatchLevel"] = (
            aws_sdk_chime_sdk_voice.types.geo_match_level.serialize_json(
                value["geo_match_level"]
            )
        )
    if "geo_match_params" in value:
        import aws_sdk_chime_sdk_voice.types.geo_match_params

        out["GeoMatchParams"] = (
            aws_sdk_chime_sdk_voice.types.geo_match_params.serialize_json(
                value["geo_match_params"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateProxySessionRequest:
    out: CreateProxySessionRequest = {}  # type: ignore[typeddict-item]
    if "ParticipantPhoneNumbers" in data:
        import aws_sdk_chime_sdk_voice.types.participant_phone_number_list

        out["participant_phone_numbers"] = (
            aws_sdk_chime_sdk_voice.types.participant_phone_number_list.deserialize_json(
                data["ParticipantPhoneNumbers"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProxySessionRequest.participant_phone_numbers required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "ExpiryMinutes" in data:
        out["expiry_minutes"] = data["ExpiryMinutes"]
    if "Capabilities" in data:
        import aws_sdk_chime_sdk_voice.types.capability_list

        out["capabilities"] = (
            aws_sdk_chime_sdk_voice.types.capability_list.deserialize_json(
                data["Capabilities"]
            )
        )
    else:
        raise DeserializationError("CreateProxySessionRequest.capabilities required")
    if "NumberSelectionBehavior" in data:
        import aws_sdk_chime_sdk_voice.types.number_selection_behavior

        out["number_selection_behavior"] = (
            aws_sdk_chime_sdk_voice.types.number_selection_behavior.deserialize_json(
                data["NumberSelectionBehavior"]
            )
        )
    if "GeoMatchLevel" in data:
        import aws_sdk_chime_sdk_voice.types.geo_match_level

        out["geo_match_level"] = (
            aws_sdk_chime_sdk_voice.types.geo_match_level.deserialize_json(
                data["GeoMatchLevel"]
            )
        )
    if "GeoMatchParams" in data:
        import aws_sdk_chime_sdk_voice.types.geo_match_params

        out["geo_match_params"] = (
            aws_sdk_chime_sdk_voice.types.geo_match_params.deserialize_json(
                data["GeoMatchParams"]
            )
        )
    return out
