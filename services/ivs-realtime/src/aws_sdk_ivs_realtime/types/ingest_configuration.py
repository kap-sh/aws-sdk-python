"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#IngestConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.ingest_configuration_arn
    import aws_sdk_ivs_realtime.types.ingest_configuration_name
    import aws_sdk_ivs_realtime.types.ingest_configuration_stage_arn
    import aws_sdk_ivs_realtime.types.ingest_configuration_state
    import aws_sdk_ivs_realtime.types.ingest_protocol
    import aws_sdk_ivs_realtime.types.participant_attributes
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.redundant_ingest
    import aws_sdk_ivs_realtime.types.redundant_ingest_credentials
    import aws_sdk_ivs_realtime.types.stream_key
    import aws_sdk_ivs_realtime.types.tags
    import aws_sdk_ivs_realtime.types.user_id


class IngestConfiguration(TypedDict):
    name: NotRequired[
        "aws_sdk_ivs_realtime.types.ingest_configuration_name.IngestConfigurationName"
    ]
    """<p>Ingest name</p>"""
    arn: "aws_sdk_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    """<p>Ingest configuration ARN.</p>"""
    ingest_protocol: "aws_sdk_ivs_realtime.types.ingest_protocol.IngestProtocol"
    """<p>Type of ingest protocol that the user employs for broadcasting.</p>"""
    stream_key: "aws_sdk_ivs_realtime.types.stream_key.StreamKey"
    """<p>Ingest-key value for the RTMP(S) protocol.</p>"""
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
    redundant_ingest_credentials: NotRequired[
        "aws_sdk_ivs_realtime.types.redundant_ingest_credentials.RedundantIngestCredentials"
    ]
    """<p>A list of redundant ingest credentials, present only when <code>redundantIngest</code> is set to <code>true</code>. See <a href=\"https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-rtmp-publishing.html#redundant-ingest\">Redundant Ingest</a> in <i>IVS RTMP Publishing</i> for details.</p>"""
    attributes: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_attributes.ParticipantAttributes"
    ]
    """<p>Application-provided attributes to to store in the IngestConfiguration and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    tags: NotRequired["aws_sdk_ivs_realtime.types.tags.Tags"]
    """<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["arn"] = value["arn"]
    import aws_sdk_ivs_realtime.types.ingest_protocol

    out["ingestProtocol"] = aws_sdk_ivs_realtime.types.ingest_protocol.serialize_json(
        value["ingest_protocol"]
    )
    out["streamKey"] = value["stream_key"]
    out["stageArn"] = value["stage_arn"]
    out["participantId"] = value["participant_id"]
    out["state"] = value["state"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    out["redundantIngest"] = value.get("redundant_ingest", False)
    if "redundant_ingest_credentials" in value:
        import aws_sdk_ivs_realtime.types.redundant_ingest_credentials

        out["redundantIngestCredentials"] = (
            aws_sdk_ivs_realtime.types.redundant_ingest_credentials.serialize_json(
                value["redundant_ingest_credentials"]
            )
        )
    if "attributes" in value:
        import aws_sdk_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            aws_sdk_ivs_realtime.types.participant_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "tags" in value:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> IngestConfiguration:
    out: IngestConfiguration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IngestConfiguration.arn required")
    if "ingestProtocol" in data:
        import aws_sdk_ivs_realtime.types.ingest_protocol

        out["ingest_protocol"] = (
            aws_sdk_ivs_realtime.types.ingest_protocol.deserialize_json(
                data["ingestProtocol"]
            )
        )
    else:
        raise DeserializationError("IngestConfiguration.ingest_protocol required")
    if "streamKey" in data:
        out["stream_key"] = data["streamKey"]
    else:
        raise DeserializationError("IngestConfiguration.stream_key required")
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("IngestConfiguration.stage_arn required")
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    else:
        raise DeserializationError("IngestConfiguration.participant_id required")
    if "state" in data:
        out["state"] = data["state"]
    else:
        raise DeserializationError("IngestConfiguration.state required")
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "redundantIngest" in data:
        out["redundant_ingest"] = data["redundantIngest"]
    else:
        out["redundant_ingest"] = False
    if "redundantIngestCredentials" in data:
        import aws_sdk_ivs_realtime.types.redundant_ingest_credentials

        out["redundant_ingest_credentials"] = (
            aws_sdk_ivs_realtime.types.redundant_ingest_credentials.deserialize_json(
                data["redundantIngestCredentials"]
            )
        )
    if "attributes" in data:
        import aws_sdk_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            aws_sdk_ivs_realtime.types.participant_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if "tags" in data:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.deserialize_json(data["tags"])
    return out
