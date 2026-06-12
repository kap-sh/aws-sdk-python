"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#IngestConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.ingest_configuration_arn
    import aws_sdk_ivs_realtime.types.ingest_configuration_name
    import aws_sdk_ivs_realtime.types.ingest_configuration_stage_arn
    import aws_sdk_ivs_realtime.types.ingest_configuration_state
    import aws_sdk_ivs_realtime.types.ingest_protocol
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.redundant_ingest
    import aws_sdk_ivs_realtime.types.user_id


class IngestConfigurationSummary(TypedDict):
    name: NotRequired[
        "aws_sdk_ivs_realtime.types.ingest_configuration_name.IngestConfigurationName"
    ]
    """<p>Ingest name.</p>"""
    arn: "aws_sdk_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>Ingest configuration ARN.</p>"""
    ingest_protocol: "aws_sdk_ivs_realtime.types.ingest_protocol.IngestProtocol"
    """<p>Type of ingest protocol that the user employs for broadcasting.</p>"""
    stage_arn: "aws_sdk_ivs_realtime.types.ingest_configuration_stage_arn.IngestConfigurationStageArn"
    """<p>ARN of the stage with which the IngestConfiguration is associated.</p>"""
    participant_id: "aws_sdk_ivs_realtime.types.participant_id.ParticipantId"
    """<p>ID of the participant within the stage.</p>"""
    state: (
        "aws_sdk_ivs_realtime.types.ingest_configuration_state.IngestConfigurationState"
    )
    """<p>State of the ingest configuration. It is <code>ACTIVE</code> if a publisher currently is publishing to the stage associated with the ingest configuration.</p>"""
    user_id: NotRequired["aws_sdk_ivs_realtime.types.user_id.UserId"]
    """<p>Customer-assigned name to help identify the participant using the IngestConfiguration; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    redundant_ingest: "aws_sdk_ivs_realtime.types.redundant_ingest.RedundantIngest"
    """<p>Indicates whether redundant ingest is enabled for the ingest configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfigurationSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    import aws_sdk_ivs_realtime.types.ingest_protocol

    out["ingestProtocol"] = aws_sdk_ivs_realtime.types.ingest_protocol.serialize_json(
        value["ingest_protocol"]
    )
    out["stageArn"] = value["stage_arn"]
    out["participantId"] = value["participant_id"]
    out["state"] = value["state"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    out["redundantIngest"] = value.get("redundant_ingest", False)
    return out


def deserialize_json(data: dict) -> IngestConfigurationSummary:
    out: IngestConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IngestConfigurationSummary.arn required")
    if "ingestProtocol" in data:
        import aws_sdk_ivs_realtime.types.ingest_protocol

        out["ingest_protocol"] = (
            aws_sdk_ivs_realtime.types.ingest_protocol.deserialize_json(
                data["ingestProtocol"]
            )
        )
    else:
        raise DeserializationError(
            "IngestConfigurationSummary.ingest_protocol required"
        )
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("IngestConfigurationSummary.stage_arn required")
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError("IngestConfigurationSummary.participant_id required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("IngestConfigurationSummary.state required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "redundantIngest" in data:
        out["redundant_ingest"] = data["redundantIngest"]
    else:
        out["redundant_ingest"] = False
    return out
