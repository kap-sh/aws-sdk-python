"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_token_attributes
    import aws_sdk_ivs_realtime.types.participant_token_capabilities
    import aws_sdk_ivs_realtime.types.participant_token_duration_minutes
    import aws_sdk_ivs_realtime.types.participant_token_user_id


class ParticipantTokenConfiguration(TypedDict):
    duration: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_token_duration_minutes.ParticipantTokenDurationMinutes"
    ]
    """<p>Duration (in minutes), after which the corresponding participant token expires. Default: 720 (12 hours).</p>"""
    user_id: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_token_user_id.ParticipantTokenUserId"
    ]
    """<p>Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    attributes: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_token_attributes.ParticipantTokenAttributes"
    ]
    """<p>Application-provided attributes to encode into the corresponding participant token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    capabilities: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_token_capabilities.ParticipantTokenCapabilities"
    ]
    """<p>Set of capabilities that the user is allowed to perform in the stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenConfiguration) -> dict:
    out: dict = {}
    if "duration" in value:
        out["duration"] = value["duration"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "attributes" in value:
        import aws_sdk_ivs_realtime.types.participant_token_attributes

        out["attributes"] = (
            aws_sdk_ivs_realtime.types.participant_token_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "capabilities" in value:
        import aws_sdk_ivs_realtime.types.participant_token_capabilities

        out["capabilities"] = (
            aws_sdk_ivs_realtime.types.participant_token_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParticipantTokenConfiguration:
    out: ParticipantTokenConfiguration = {}  # type: ignore[typeddict-item]
    if "duration" in data:
        out["duration"] = data["duration"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "attributes" in data:
        import aws_sdk_ivs_realtime.types.participant_token_attributes

        out["attributes"] = (
            aws_sdk_ivs_realtime.types.participant_token_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if "capabilities" in data:
        import aws_sdk_ivs_realtime.types.participant_token_capabilities

        out["capabilities"] = (
            aws_sdk_ivs_realtime.types.participant_token_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    return out
