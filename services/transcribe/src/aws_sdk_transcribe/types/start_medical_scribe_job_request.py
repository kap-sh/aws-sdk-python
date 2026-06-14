"""Generated from Smithy shape ``com.amazonaws.transcribe#StartMedicalScribeJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_transcribe.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transcribe.types.data_access_role_arn
    import aws_sdk_transcribe.types.kms_encryption_context_map
    import aws_sdk_transcribe.types.kms_key_id
    import aws_sdk_transcribe.types.media
    import aws_sdk_transcribe.types.medical_scribe_channel_definitions
    import aws_sdk_transcribe.types.medical_scribe_context
    import aws_sdk_transcribe.types.medical_scribe_settings
    import aws_sdk_transcribe.types.output_bucket_name
    import aws_sdk_transcribe.types.tag_list
    import aws_sdk_transcribe.types.transcription_job_name


class StartMedicalScribeJobRequest(TypedDict):
    medical_scribe_job_name: (
        "aws_sdk_transcribe.types.transcription_job_name.TranscriptionJobName"
    )
    """<p>A unique name, chosen by you, for your Medical Scribe job.</p> <p>This name is case sensitive, cannot contain spaces, and must be unique within an Amazon Web Services account. If you try to create a new job with the same name as an existing job, you get a <code>ConflictException</code> error.</p>"""
    media: "aws_sdk_transcribe.types.media.Media"
    output_bucket_name: "aws_sdk_transcribe.types.output_bucket_name.OutputBucketName"
    r"""<p>The name of the Amazon S3 bucket where you want your Medical Scribe output stored. Do not include the <code>S3://</code> prefix of the specified bucket.</p> <p>Note that the role specified in the <code>DataAccessRoleArn</code> request parameter must have permission to use the specified location. You can change Amazon S3 permissions using the <a href=\"https://console.aws.amazon.com/s3\">Amazon Web Services Management Console</a>. See also <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user\">Permissions Required for IAM User Roles</a>.</p>"""
    output_encryption_kms_key_id: NotRequired[
        "aws_sdk_transcribe.types.kms_key_id.KMSKeyId"
    ]
    r"""<p>The Amazon Resource Name (ARN) of a KMS key that you want to use to encrypt your Medical Scribe output.</p> <p>KMS key ARNs have the format <code>arn:partition:kms:region:account:key/key-id</code>. For example: <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\"> KMS key ARNs</a>.</p> <p>If you do not specify an encryption key, your output is encrypted with the default Amazon S3 key (SSE-S3).</p> <p>Note that the role making the request and the role specified in the <code>DataAccessRoleArn</code> request parameter (if present) must have permission to use the specified KMS key.</p>"""
    kms_encryption_context: NotRequired[
        "aws_sdk_transcribe.types.kms_encryption_context_map.KMSEncryptionContextMap"
    ]
    r"""<p>A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context\">KMS encryption context</a> and <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/symmetric-asymmetric.html\">Asymmetric keys in KMS</a>.</p>"""
    data_access_role_arn: (
        "aws_sdk_transcribe.types.data_access_role_arn.DataAccessRoleArn"
    )
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that has permissions to access the Amazon S3 bucket that contains your input files, write to the output bucket, and use your KMS key if supplied. If the role that you specify doesn’t have the appropriate permissions your request fails.</p> <p>IAM role ARNs have the format <code>arn:partition:iam::account:role/role-name-with-path</code>. For example: <code>arn:aws:iam::111122223333:role/Admin</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns\">IAM ARNs</a>.</p>"""
    settings: "aws_sdk_transcribe.types.medical_scribe_settings.MedicalScribeSettings"
    """<p>Makes it possible to control how your Medical Scribe job is processed using a <code>MedicalScribeSettings</code> object. Specify <code>ChannelIdentification</code> if <code>ChannelDefinitions</code> are set. Enabled <code>ShowSpeakerLabels</code> if <code>ChannelIdentification</code> and <code>ChannelDefinitions</code> are not set. One and only one of <code>ChannelIdentification</code> and <code>ShowSpeakerLabels</code> must be set. If <code>ShowSpeakerLabels</code> is set, <code>MaxSpeakerLabels</code> must also be set. Use <code>Settings</code> to specify a vocabulary or vocabulary filter or both using <code>VocabularyName</code>, <code>VocabularyFilterName</code>. <code>VocabularyFilterMethod</code> must be specified if <code>VocabularyFilterName</code> is set. </p>"""
    channel_definitions: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_channel_definitions.MedicalScribeChannelDefinitions"
    ]
    """<p>Makes it possible to specify which speaker is on which channel. For example, if the clinician is the first participant to speak, you would set <code>ChannelId</code> of the first <code>ChannelDefinition</code> in the list to <code>0</code> (to indicate the first channel) and <code>ParticipantRole</code> to <code>CLINICIAN</code> (to indicate that it's the clinician speaking). Then you would set the <code>ChannelId</code> of the second <code>ChannelDefinition</code> in the list to <code>1</code> (to indicate the second channel) and <code>ParticipantRole</code> to <code>PATIENT</code> (to indicate that it's the patient speaking). </p>"""
    tags: NotRequired["aws_sdk_transcribe.types.tag_list.TagList"]
    r"""<p>Adds one or more custom tags, each in the form of a key:value pair, to the Medical Scribe job.</p> <p>To learn more about using tags with Amazon Transcribe, refer to <a href=\"https://docs.aws.amazon.com/transcribe/latest/dg/tagging.html\">Tagging resources</a>.</p>"""
    medical_scribe_context: NotRequired[
        "aws_sdk_transcribe.types.medical_scribe_context.MedicalScribeContext"
    ]
    """<p>The <code>MedicalScribeContext</code> object that contains contextual information which is used during clinical note generation to add relevant context to the note.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMedicalScribeJobRequest) -> dict:
    out: dict = {}
    import aws_sdk_transcribe.types.media

    out["Media"] = aws_sdk_transcribe.types.media.serialize_aws_json_1_1(value["media"])
    out["OutputBucketName"] = value["output_bucket_name"]
    if "output_encryption_kms_key_id" in value:
        out["OutputEncryptionKMSKeyId"] = value["output_encryption_kms_key_id"]
    if "kms_encryption_context" in value:
        import aws_sdk_transcribe.types.kms_encryption_context_map

        out["KMSEncryptionContext"] = (
            aws_sdk_transcribe.types.kms_encryption_context_map.serialize_aws_json_1_1(
                value["kms_encryption_context"]
            )
        )
    out["DataAccessRoleArn"] = value["data_access_role_arn"]
    import aws_sdk_transcribe.types.medical_scribe_settings

    out["Settings"] = (
        aws_sdk_transcribe.types.medical_scribe_settings.serialize_aws_json_1_1(
            value["settings"]
        )
    )
    if "channel_definitions" in value:
        import aws_sdk_transcribe.types.medical_scribe_channel_definitions

        out["ChannelDefinitions"] = (
            aws_sdk_transcribe.types.medical_scribe_channel_definitions.serialize_aws_json_1_1(
                value["channel_definitions"]
            )
        )
    if "tags" in value:
        import aws_sdk_transcribe.types.tag_list

        out["Tags"] = aws_sdk_transcribe.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "medical_scribe_context" in value:
        import aws_sdk_transcribe.types.medical_scribe_context

        out["MedicalScribeContext"] = (
            aws_sdk_transcribe.types.medical_scribe_context.serialize_aws_json_1_1(
                value["medical_scribe_context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMedicalScribeJobRequest:
    out: StartMedicalScribeJobRequest = {}  # type: ignore[typeddict-item]
    if "Media" in data:
        import aws_sdk_transcribe.types.media

        out["media"] = aws_sdk_transcribe.types.media.deserialize_aws_json_1_1(
            data["Media"]
        )
    else:
        raise DeserializationError("StartMedicalScribeJobRequest.media required")
    if "OutputBucketName" in data:
        out["output_bucket_name"] = data["OutputBucketName"]
    else:
        raise DeserializationError(
            "StartMedicalScribeJobRequest.output_bucket_name required"
        )
    if "OutputEncryptionKMSKeyId" in data:
        out["output_encryption_kms_key_id"] = data["OutputEncryptionKMSKeyId"]
    if "KMSEncryptionContext" in data:
        import aws_sdk_transcribe.types.kms_encryption_context_map

        out["kms_encryption_context"] = (
            aws_sdk_transcribe.types.kms_encryption_context_map.deserialize_aws_json_1_1(
                data["KMSEncryptionContext"]
            )
        )
    if "DataAccessRoleArn" in data:
        out["data_access_role_arn"] = data["DataAccessRoleArn"]
    else:
        raise DeserializationError(
            "StartMedicalScribeJobRequest.data_access_role_arn required"
        )
    if "Settings" in data:
        import aws_sdk_transcribe.types.medical_scribe_settings

        out["settings"] = (
            aws_sdk_transcribe.types.medical_scribe_settings.deserialize_aws_json_1_1(
                data["Settings"]
            )
        )
    else:
        raise DeserializationError("StartMedicalScribeJobRequest.settings required")
    if "ChannelDefinitions" in data:
        import aws_sdk_transcribe.types.medical_scribe_channel_definitions

        out["channel_definitions"] = (
            aws_sdk_transcribe.types.medical_scribe_channel_definitions.deserialize_aws_json_1_1(
                data["ChannelDefinitions"]
            )
        )
    if "Tags" in data:
        import aws_sdk_transcribe.types.tag_list

        out["tags"] = aws_sdk_transcribe.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "MedicalScribeContext" in data:
        import aws_sdk_transcribe.types.medical_scribe_context

        out["medical_scribe_context"] = (
            aws_sdk_transcribe.types.medical_scribe_context.deserialize_aws_json_1_1(
                data["MedicalScribeContext"]
            )
        )
    return out
