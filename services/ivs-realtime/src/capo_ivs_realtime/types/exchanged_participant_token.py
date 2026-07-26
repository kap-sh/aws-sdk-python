"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ExchangedParticipantToken``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_token_attributes
    import capo_ivs_realtime.types.participant_token_capabilities
    import capo_ivs_realtime.types.participant_token_expiration_time
    import capo_ivs_realtime.types.participant_token_user_id


class ExchangedParticipantToken(TypedDict, closed=True):
    capabilities: NotRequired[
        "capo_ivs_realtime.types.participant_token_capabilities.ParticipantTokenCapabilities"
    ]
    """<p>Set of capabilities that the user is allowed to perform in the stage.</p>"""
    attributes: NotRequired[
        "capo_ivs_realtime.types.participant_token_attributes.ParticipantTokenAttributes"
    ]
    """<p>Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    user_id: NotRequired[
        "capo_ivs_realtime.types.participant_token_user_id.ParticipantTokenUserId"
    ]
    """<p>Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    expiration_time: NotRequired[
        "capo_ivs_realtime.types.participant_token_expiration_time.ParticipantTokenExpirationTime"
    ]
    """<p>ISO 8601 timestamp (returned as a string) for when this token expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExchangedParticipantToken) -> dict:
    out: dict = {}
    if "capabilities" in value:
        import capo_ivs_realtime.types.participant_token_capabilities

        out["capabilities"] = (
            capo_ivs_realtime.types.participant_token_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    if "attributes" in value:
        import capo_ivs_realtime.types.participant_token_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_token_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "expiration_time" in value:
        import capo_ivs_realtime.types.participant_token_expiration_time

        out["expirationTime"] = (
            capo_ivs_realtime.types.participant_token_expiration_time.serialize_json(
                value["expiration_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> ExchangedParticipantToken:
    out: ExchangedParticipantToken = {}  # type: ignore[typeddict-item]
    if "capabilities" in data:
        import capo_ivs_realtime.types.participant_token_capabilities

        out["capabilities"] = (
            capo_ivs_realtime.types.participant_token_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    if "attributes" in data:
        import capo_ivs_realtime.types.participant_token_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_token_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "expirationTime" in data:
        import capo_ivs_realtime.types.participant_token_expiration_time

        out["expiration_time"] = (
            capo_ivs_realtime.types.participant_token_expiration_time.deserialize_json(
                data["expirationTime"]
            )
        )
    return out
