"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DescribeSecretResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.deleted_date_type
    import aws_sdk_secrets_manager.types.description_type
    import aws_sdk_secrets_manager.types.external_secret_rotation_metadata_type
    import aws_sdk_secrets_manager.types.kms_key_id_type
    import aws_sdk_secrets_manager.types.last_accessed_date_type
    import aws_sdk_secrets_manager.types.last_changed_date_type
    import aws_sdk_secrets_manager.types.last_rotated_date_type
    import aws_sdk_secrets_manager.types.medea_type_type
    import aws_sdk_secrets_manager.types.next_rotation_date_type
    import aws_sdk_secrets_manager.types.owning_service_type
    import aws_sdk_secrets_manager.types.region_type
    import aws_sdk_secrets_manager.types.replication_status_list_type
    import aws_sdk_secrets_manager.types.role_arn_type
    import aws_sdk_secrets_manager.types.rotation_enabled_type
    import aws_sdk_secrets_manager.types.rotation_lambda_arn_type
    import aws_sdk_secrets_manager.types.rotation_rules_type
    import aws_sdk_secrets_manager.types.secret_arn_type
    import aws_sdk_secrets_manager.types.secret_name_type
    import aws_sdk_secrets_manager.types.secret_versions_to_stages_map_type
    import aws_sdk_secrets_manager.types.tag_list_type
    import aws_sdk_secrets_manager.types.timestamp_type


class DescribeSecretResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The name of the secret.</p>"""
    type: NotRequired["aws_sdk_secrets_manager.types.medea_type_type.MedeaTypeType"]
    """<p>The exact string that identifies the partner that holds the external secret. For more information, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html\">Using Secrets Manager managed external secrets</a>.</p>"""
    description: NotRequired[
        "aws_sdk_secrets_manager.types.description_type.DescriptionType"
    ]
    """<p>The description of the secret.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_secrets_manager.types.kms_key_id_type.KmsKeyIdType"
    ]
    """<p>The key ID or alias ARN of the KMS key that Secrets Manager uses to encrypt the secret value. If the secret is encrypted with the Amazon Web Services managed key <code>aws/secretsmanager</code>, this field is omitted. Secrets created using the console use an KMS key ID.</p>"""
    rotation_enabled: (
        "aws_sdk_secrets_manager.types.rotation_enabled_type.RotationEnabledType"
    )
    """<p>Specifies whether automatic rotation is turned on for this secret. If the secret has never been configured for rotation, Secrets Manager returns null.</p> <p>To turn on rotation, use <a>RotateSecret</a>. To turn off rotation, use <a>CancelRotateSecret</a>.</p>"""
    rotation_lambda_arn: NotRequired[
        "aws_sdk_secrets_manager.types.rotation_lambda_arn_type.RotationLambdaARNType"
    ]
    """<p>The ARN of the Lambda function that Secrets Manager invokes to rotate the secret. </p>"""
    rotation_rules: NotRequired[
        "aws_sdk_secrets_manager.types.rotation_rules_type.RotationRulesType"
    ]
    """<p>The rotation schedule and Lambda function for this secret. If the secret previously had rotation turned on, but it is now turned off, this field shows the previous rotation schedule and rotation function. If the secret never had rotation turned on, this field is omitted.</p>"""
    external_secret_rotation_metadata: NotRequired[
        "aws_sdk_secrets_manager.types.external_secret_rotation_metadata_type.ExternalSecretRotationMetadataType"
    ]
    """<p>The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html\">Managed external secrets partners</a>.</p>"""
    external_secret_rotation_role_arn: NotRequired[
        "aws_sdk_secrets_manager.types.role_arn_type.RoleARNType"
    ]
    """<p>The Amazon Resource Name (ARN) of the role that allows Secrets Manager to rotate a secret held by a third-party partner. For more information, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html\">Security and permissions</a>.</p>"""
    last_rotated_date: NotRequired[
        "aws_sdk_secrets_manager.types.last_rotated_date_type.LastRotatedDateType"
    ]
    """<p>The last date and time that Secrets Manager rotated the secret. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null.</p>"""
    last_changed_date: NotRequired[
        "aws_sdk_secrets_manager.types.last_changed_date_type.LastChangedDateType"
    ]
    """<p>The last date and time that this secret was modified in any way.</p>"""
    last_accessed_date: NotRequired[
        "aws_sdk_secrets_manager.types.last_accessed_date_type.LastAccessedDateType"
    ]
    """<p>The date that the secret was last accessed in the Region. This field is omitted if the secret has never been retrieved in the Region.</p>"""
    deleted_date: NotRequired[
        "aws_sdk_secrets_manager.types.deleted_date_type.DeletedDateType"
    ]
    """<p>The date the secret is scheduled for deletion. If it is not scheduled for deletion, this field is omitted. When you delete a secret, Secrets Manager requires a recovery window of at least 7 days before deleting the secret. Some time after the deleted date, Secrets Manager deletes the secret, including all of its versions.</p> <p>If a secret is scheduled for deletion, then its details, including the encrypted secret value, is not accessible. To cancel a scheduled deletion and restore access to the secret, use <a>RestoreSecret</a>.</p>"""
    next_rotation_date: NotRequired[
        "aws_sdk_secrets_manager.types.next_rotation_date_type.NextRotationDateType"
    ]
    """<p>The next rotation is scheduled to occur on or before this date. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null. If rotation fails, Secrets Manager retries the entire rotation process multiple times. If rotation is unsuccessful, this date may be in the past.</p> <p>This date represents the latest date that rotation will occur, but it is not an approximate rotation date. In some cases, for example if you turn off automatic rotation and then turn it back on, the next rotation may occur much sooner than this date.</p>"""
    tags: NotRequired["aws_sdk_secrets_manager.types.tag_list_type.TagListType"]
    """<p>The list of tags attached to the secret. To add tags to a secret, use <a>TagResource</a>. To remove tags, use <a>UntagResource</a>.</p>"""
    version_ids_to_stages: NotRequired[
        "aws_sdk_secrets_manager.types.secret_versions_to_stages_map_type.SecretVersionsToStagesMapType"
    ]
    """<p>A list of the versions of the secret that have staging labels attached. Versions that don't have staging labels are considered deprecated and Secrets Manager can delete them.</p> <p>Secrets Manager uses staging labels to indicate the status of a secret version during rotation. The three staging labels for rotation are: </p> <ul> <li> <p> <code>AWSCURRENT</code>, which indicates the current version of the secret.</p> </li> <li> <p> <code>AWSPENDING</code>, which indicates the version of the secret that contains new secret information that will become the next current version when rotation finishes.</p> <p>During rotation, Secrets Manager creates an <code>AWSPENDING</code> version ID before creating the new secret version. To check if a secret version exists, call <a>GetSecretValue</a>.</p> </li> <li> <p> <code>AWSPREVIOUS</code>, which indicates the previous current version of the secret. You can use this as the <i>last known good</i> version.</p> </li> </ul> <p>For more information about rotation and staging labels, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html\">How rotation works</a>.</p>"""
    owning_service: NotRequired[
        "aws_sdk_secrets_manager.types.owning_service_type.OwningServiceType"
    ]
    """<p>The ID of the service that created this secret. For more information, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html\">Secrets managed by other Amazon Web Services services</a>.</p>"""
    created_date: NotRequired[
        "aws_sdk_secrets_manager.types.timestamp_type.TimestampType"
    ]
    """<p>The date the secret was created.</p>"""
    primary_region: NotRequired["aws_sdk_secrets_manager.types.region_type.RegionType"]
    """<p>The Region the secret is in. If a secret is replicated to other Regions, the replicas are listed in <code>ReplicationStatus</code>. </p>"""
    replication_status: NotRequired[
        "aws_sdk_secrets_manager.types.replication_status_list_type.ReplicationStatusListType"
    ]
    """<p>A list of the replicas of this secret and their status: </p> <ul> <li> <p> <code>Failed</code>, which indicates that the replica was not created.</p> </li> <li> <p> <code>InProgress</code>, which indicates that Secrets Manager is in the process of creating the replica.</p> </li> <li> <p> <code>InSync</code>, which indicates that the replica was created.</p> </li> </ul>"""
