"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#ProxySession``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_voice.types.capability_list
    import aws_sdk_chime_sdk_voice.types.geo_match_level
    import aws_sdk_chime_sdk_voice.types.geo_match_params
    import aws_sdk_chime_sdk_voice.types.iso8601_timestamp
    import aws_sdk_chime_sdk_voice.types.non_empty_string128
    import aws_sdk_chime_sdk_voice.types.number_selection_behavior
    import aws_sdk_chime_sdk_voice.types.participants
    import aws_sdk_chime_sdk_voice.types.positive_integer
    import aws_sdk_chime_sdk_voice.types.proxy_session_status
    import aws_sdk_chime_sdk_voice.types.string128


class ProxySession(TypedDict):
    voice_connector_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    ]
    """<p>The Voice Connector ID.</p>"""
    proxy_session_id: NotRequired[
        "aws_sdk_chime_sdk_voice.types.non_empty_string128.NonEmptyString128"
    ]
    """<p>The proxy session ID.</p>"""
    name: NotRequired["aws_sdk_chime_sdk_voice.types.string128.String128"]
    """<p>The proxy session name.</p>"""
    status: NotRequired[
        "aws_sdk_chime_sdk_voice.types.proxy_session_status.ProxySessionStatus"
    ]
    """<p>The proxy session status.</p>"""
    expiry_minutes: NotRequired[
        "aws_sdk_chime_sdk_voice.types.positive_integer.PositiveInteger"
    ]
    """<p>The number of minutes allowed for the proxy session.</p>"""
    capabilities: NotRequired[
        "aws_sdk_chime_sdk_voice.types.capability_list.CapabilityList"
    ]
    """<p>The proxy session capabilities.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The created time stamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The updated time stamp, in ISO 8601 format.</p>"""
    ended_timestamp: NotRequired[
        "aws_sdk_chime_sdk_voice.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The ended time stamp, in ISO 8601 format.</p>"""
    participants: NotRequired["aws_sdk_chime_sdk_voice.types.participants.Participants"]
    """<p>The proxy session participants.</p>"""
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
def serialize_json(value: ProxySession) -> dict:
    out: dict = {}
    if "voice_connector_id" in value:
        out["VoiceConnectorId"] = value["voice_connector_id"]
    if "proxy_session_id" in value:
        out["ProxySessionId"] = value["proxy_session_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_chime_sdk_voice.types.proxy_session_status

        out["Status"] = (
            aws_sdk_chime_sdk_voice.types.proxy_session_status.serialize_json(
                value["status"]
            )
        )
    if "expiry_minutes" in value:
        out["ExpiryMinutes"] = value["expiry_minutes"]
    if "capabilities" in value:
        import aws_sdk_chime_sdk_voice.types.capability_list

        out["Capabilities"] = (
            aws_sdk_chime_sdk_voice.types.capability_list.serialize_json(
                value["capabilities"]
            )
        )
    if "created_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    if "ended_timestamp" in value:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["EndedTimestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.serialize_json(
                value["ended_timestamp"]
            )
        )
    if "participants" in value:
        import aws_sdk_chime_sdk_voice.types.participants

        out["Participants"] = aws_sdk_chime_sdk_voice.types.participants.serialize_json(
            value["participants"]
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


def deserialize_json(data: dict) -> ProxySession:
    out: ProxySession = {}  # type: ignore[typeddict-item]
    if "VoiceConnectorId" in data:
        out["voice_connector_id"] = data["VoiceConnectorId"]
    if "ProxySessionId" in data:
        out["proxy_session_id"] = data["ProxySessionId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_chime_sdk_voice.types.proxy_session_status

        out["status"] = (
            aws_sdk_chime_sdk_voice.types.proxy_session_status.deserialize_json(
                data["Status"]
            )
        )
    if "ExpiryMinutes" in data:
        out["expiry_minutes"] = data["ExpiryMinutes"]
    if "Capabilities" in data:
        import aws_sdk_chime_sdk_voice.types.capability_list

        out["capabilities"] = (
            aws_sdk_chime_sdk_voice.types.capability_list.deserialize_json(
                data["Capabilities"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["created_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "UpdatedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["updated_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    if "EndedTimestamp" in data:
        import aws_sdk_chime_sdk_voice.types.iso8601_timestamp

        out["ended_timestamp"] = (
            aws_sdk_chime_sdk_voice.types.iso8601_timestamp.deserialize_json(
                data["EndedTimestamp"]
            )
        )
    if "Participants" in data:
        import aws_sdk_chime_sdk_voice.types.participants

        out["participants"] = (
            aws_sdk_chime_sdk_voice.types.participants.deserialize_json(
                data["Participants"]
            )
        )
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
