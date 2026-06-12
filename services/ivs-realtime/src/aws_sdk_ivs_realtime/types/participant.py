"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#Participant``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.ingest_configuration_arn
    import aws_sdk_ivs_realtime.types.participant_attributes
    import aws_sdk_ivs_realtime.types.participant_client_attribute
    import aws_sdk_ivs_realtime.types.participant_id
    import aws_sdk_ivs_realtime.types.participant_protocol
    import aws_sdk_ivs_realtime.types.participant_recording_s3_bucket_name
    import aws_sdk_ivs_realtime.types.participant_recording_s3_prefix
    import aws_sdk_ivs_realtime.types.participant_recording_state
    import aws_sdk_ivs_realtime.types.participant_state
    import aws_sdk_ivs_realtime.types.published
    import aws_sdk_ivs_realtime.types.redundant_ingest
    import aws_sdk_ivs_realtime.types.replication_state
    import aws_sdk_ivs_realtime.types.replication_type
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.stage_session_id
    import aws_sdk_ivs_realtime.types.time
    import aws_sdk_ivs_realtime.types.user_id


class Participant(TypedDict):
    participant_id: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_id.ParticipantId"
    ]
    """<p>Unique identifier for this participant, assigned by IVS.</p>"""
    user_id: NotRequired["aws_sdk_ivs_realtime.types.user_id.UserId"]
    """<p>Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information</i>.</p>"""
    state: NotRequired["aws_sdk_ivs_realtime.types.participant_state.ParticipantState"]
    """<p>Whether the participant is connected to or disconnected from the stage.</p>"""
    first_join_time: NotRequired["aws_sdk_ivs_realtime.types.time.Time"]
    """<p>ISO 8601 timestamp (returned as a string) when the participant first joined the stage session.</p>"""
    attributes: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_attributes.ParticipantAttributes"
    ]
    """<p>Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information</i>.</p>"""
    published: "aws_sdk_ivs_realtime.types.published.Published"
    """<p>Whether the participant ever published to the stage session.</p>"""
    isp_name: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_client_attribute.ParticipantClientAttribute"
    ]
    """<p>The participant’s Internet Service Provider.</p>"""
    os_name: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_client_attribute.ParticipantClientAttribute"
    ]
    """<p>The participant’s operating system.</p>"""
    os_version: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_client_attribute.ParticipantClientAttribute"
    ]
    """<p>The participant’s operating system version.</p>"""
    browser_name: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_client_attribute.ParticipantClientAttribute"
    ]
    """<p>The participant’s browser.</p>"""
    browser_version: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_client_attribute.ParticipantClientAttribute"
    ]
    """<p>The participant’s browser version.</p>"""
    sdk_version: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_client_attribute.ParticipantClientAttribute"
    ]
    """<p>The participant’s SDK version.</p>"""
    recording_s3_bucket_name: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_recording_s3_bucket_name.ParticipantRecordingS3BucketName"
    ]
    """<p>Name of the S3 bucket to where the participant is being recorded, if individual participant recording is enabled, or <code>\"\"</code> (empty string), if recording is not enabled.</p>"""
    recording_s3_prefix: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_recording_s3_prefix.ParticipantRecordingS3Prefix"
    ]
    """<p>S3 prefix of the S3 bucket where the participant is being recorded, if individual participant recording is enabled, or <code>\"\"</code> (empty string), if recording is not enabled. If individual participant recording merge is enabled, and if a stage publisher disconnects from a stage and then reconnects, IVS tries to record to the same S3 prefix as the previous session. See <a href=\"/ivs/latest/RealTimeUserGuide/rt-individual-participant-recording.html#ind-part-rec-merge-frag\"> Merge Fragmented Individual Participant Recordings</a>.</p>"""
    recording_state: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_recording_state.ParticipantRecordingState"
    ]
    """<p>The participant’s recording state.</p>"""
    protocol: NotRequired[
        "aws_sdk_ivs_realtime.types.participant_protocol.ParticipantProtocol"
    ]
    """<p>Type of ingest protocol that the participant employs for broadcasting.</p>"""
    replication_type: NotRequired[
        "aws_sdk_ivs_realtime.types.replication_type.ReplicationType"
    ]
    """<p>Indicates if the participant has been replicated to another stage or is a replica from another stage. Default: <code>NONE</code>. </p>"""
    replication_state: NotRequired[
        "aws_sdk_ivs_realtime.types.replication_state.ReplicationState"
    ]
    """<p>The participant's replication state.</p>"""
    source_stage_arn: NotRequired["aws_sdk_ivs_realtime.types.stage_arn.StageArn"]
    """<p>Source stage ARN from which this participant is replicated, if <code>replicationType</code> is <code>REPLICA</code>. </p>"""
    source_session_id: NotRequired[
        "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    ]
    """<p>ID of the session within the source stage, if <code>replicationType</code> is <code>REPLICA</code>.</p>"""
    redundant_ingest: "aws_sdk_ivs_realtime.types.redundant_ingest.RedundantIngest"
    """<p>Indicates whether redundant ingest is enabled for the participant.</p>"""
    ingest_configuration_arn: NotRequired[
        "aws_sdk_ivs_realtime.types.ingest_configuration_arn.IngestConfigurationArn"
    ]
    """<p>The participant’s ingest configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Participant) -> dict:
    out: dict = {}
    if "participant_id" in value:
        out["participantId"] = value["participant_id"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "state" in value:
        out["state"] = value["state"]
    if "first_join_time" in value:
        import aws_sdk_ivs_realtime.types.time

        out["firstJoinTime"] = aws_sdk_ivs_realtime.types.time.serialize_json(
            value["first_join_time"]
        )
    if "attributes" in value:
        import aws_sdk_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            aws_sdk_ivs_realtime.types.participant_attributes.serialize_json(
                value["attributes"]
            )
        )
    out["published"] = value.get("published", False)
    if "isp_name" in value:
        out["ispName"] = value["isp_name"]
    if "os_name" in value:
        out["osName"] = value["os_name"]
    if "os_version" in value:
        out["osVersion"] = value["os_version"]
    if "browser_name" in value:
        out["browserName"] = value["browser_name"]
    if "browser_version" in value:
        out["browserVersion"] = value["browser_version"]
    if "sdk_version" in value:
        out["sdkVersion"] = value["sdk_version"]
    if "recording_s3_bucket_name" in value:
        out["recordingS3BucketName"] = value["recording_s3_bucket_name"]
    if "recording_s3_prefix" in value:
        out["recordingS3Prefix"] = value["recording_s3_prefix"]
    if "recording_state" in value:
        out["recordingState"] = value["recording_state"]
    if "protocol" in value:
        import aws_sdk_ivs_realtime.types.participant_protocol

        out["protocol"] = (
            aws_sdk_ivs_realtime.types.participant_protocol.serialize_json(
                value["protocol"]
            )
        )
    if "replication_type" in value:
        out["replicationType"] = value["replication_type"]
    if "replication_state" in value:
        out["replicationState"] = value["replication_state"]
    if "source_stage_arn" in value:
        out["sourceStageArn"] = value["source_stage_arn"]
    if "source_session_id" in value:
        out["sourceSessionId"] = value["source_session_id"]
    out["redundantIngest"] = value.get("redundant_ingest", False)
    if "ingest_configuration_arn" in value:
        out["ingestConfigurationArn"] = value["ingest_configuration_arn"]
    return out


def deserialize_json(data: dict) -> Participant:
    out: Participant = {}  # type: ignore[typeddict-item]
    if "participantId" in data:
        out["participant_id"] = data["participantId"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "state" in data:
        out["state"] = data["state"]
    if "firstJoinTime" in data:
        import aws_sdk_ivs_realtime.types.time

        out["first_join_time"] = aws_sdk_ivs_realtime.types.time.deserialize_json(
            data["firstJoinTime"]
        )
    if "attributes" in data:
        import aws_sdk_ivs_realtime.types.participant_attributes

        out["attributes"] = (
            aws_sdk_ivs_realtime.types.participant_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if "published" in data:
        out["published"] = data["published"]
    else:
        out["published"] = False
    if "ispName" in data:
        out["isp_name"] = data["ispName"]
    if "osName" in data:
        out["os_name"] = data["osName"]
    if "osVersion" in data:
        out["os_version"] = data["osVersion"]
    if "browserName" in data:
        out["browser_name"] = data["browserName"]
    if "browserVersion" in data:
        out["browser_version"] = data["browserVersion"]
    if "sdkVersion" in data:
        out["sdk_version"] = data["sdkVersion"]
    if "recordingS3BucketName" in data:
        out["recording_s3_bucket_name"] = data["recordingS3BucketName"]
    if "recordingS3Prefix" in data:
        out["recording_s3_prefix"] = data["recordingS3Prefix"]
    if "recordingState" in data:
        out["recording_state"] = data["recordingState"]
    if "protocol" in data:
        import aws_sdk_ivs_realtime.types.participant_protocol

        out["protocol"] = (
            aws_sdk_ivs_realtime.types.participant_protocol.deserialize_json(
                data["protocol"]
            )
        )
    if "replicationType" in data:
        out["replication_type"] = data["replicationType"]
    if "replicationState" in data:
        out["replication_state"] = data["replicationState"]
    if "sourceStageArn" in data:
        out["source_stage_arn"] = data["sourceStageArn"]
    if "sourceSessionId" in data:
        out["source_session_id"] = data["sourceSessionId"]
    if "redundantIngest" in data:
        out["redundant_ingest"] = data["redundantIngest"]
    else:
        out["redundant_ingest"] = False
    if "ingestConfigurationArn" in data:
        out["ingest_configuration_arn"] = data["ingestConfigurationArn"]
    return out
