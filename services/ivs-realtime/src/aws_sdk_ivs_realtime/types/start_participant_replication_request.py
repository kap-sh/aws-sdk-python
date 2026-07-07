"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StartParticipantReplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.participant_attributes
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.reconnect_window_seconds
    import aws_sdk_ivs_realtime.types.stage_arn


class StartParticipantReplicationRequest(TypedDict, closed=True):
    source_stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage where the participant is publishing.</p>"""
    destination_stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage to which the participant will be replicated.</p>"""
    participant_id: "aws_sdk_ivs_realtime.types.participant_id.ParticipantId"
    r"""<p>Participant ID of the publisher that will be replicated. This is assigned by IVS and returned by <a>CreateParticipantToken</a> or the <code>jti</code> (JWT ID) used to <a href=\"https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html#getting-started-distribute-tokens-self-signed\">create a self signed token</a>. </p>"""
    reconnect_window_seconds: NotRequired[
        "aws_sdk_ivs_realtime.types.reconnect_window_seconds.ReconnectWindowSeconds"
    ]
    """<p>If the participant disconnects and then reconnects within the specified interval, replication will continue to be <code>ACTIVE</code>. Default: 0.</p>"""
    attributes: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_attributes.ParticipantAttributes"
    ]
    """<p>Application-provided attributes to set on the replicated participant in the destination stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p> <p>These attributes are merged with any attributes set for this participant when creating the token. If there is overlap in keys, the values in these attributes are replaced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartParticipantReplicationRequest) -> dict:
    out: dict = {}
    out["sourceStageArn"] = value["source_stage_arn"]
    out["destinationStageArn"] = value["destination_stage_arn"]
    out["participantId"] = value["participant_id"]
    if "reconnect_window_seconds" in value:
        out["reconnectWindowSeconds"] = value["reconnect_window_seconds"]
    if "attributes" in value:
        import aws_sdk_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            aws_sdk_ivs_realtime.types.participant_attributes.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartParticipantReplicationRequest:
    out: StartParticipantReplicationRequest = {}  # type: ignore[typeddict-item]
    if "sourceStageArn" in data:
        out["source_stage_arn"] = data["sourceStageArn"]
    else:
        raise DeserializationError(
            "StartParticipantReplicationRequest.source_stage_arn required"
        )
    if "destinationStageArn" in data:
        out["destination_stage_arn"] = data["destinationStageArn"]
    else:
        raise DeserializationError(
            "StartParticipantReplicationRequest.destination_stage_arn required"
        )
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError(
            "StartParticipantReplicationRequest.participant_id required"
        )
    if "reconnectWindowSeconds" in data:
        out["reconnect_window_seconds"] = data["reconnectWindowSeconds"]
    if "attributes" in data:
        import aws_sdk_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            aws_sdk_ivs_realtime.types.participant_attributes.deserialize_json(
                data["attributes"]
            )
        )
    return out
