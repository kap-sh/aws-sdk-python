"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretListEntry``."""

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
    import aws_sdk_secrets_manager.types.role_arn_type
    import aws_sdk_secrets_manager.types.rotation_enabled_type
    import aws_sdk_secrets_manager.types.rotation_lambda_arn_type
    import aws_sdk_secrets_manager.types.rotation_rules_type
    import aws_sdk_secrets_manager.types.secret_arn_type
    import aws_sdk_secrets_manager.types.secret_name_type
    import aws_sdk_secrets_manager.types.secret_versions_to_stages_map_type
    import aws_sdk_secrets_manager.types.tag_list_type
    import aws_sdk_secrets_manager.types.timestamp_type


class SecretListEntry(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The Amazon Resource Name (ARN) of the secret.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The friendly name of the secret. </p>"""
    type: NotRequired["aws_sdk_secrets_manager.types.medea_type_type.MedeaTypeType"]
    """<p>The exact string that identifies the third-party partner that holds the external secret. For more information, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html\">Managed external secret partners</a>.</p>"""
    description: NotRequired[
        "aws_sdk_secrets_manager.types.description_type.DescriptionType"
    ]
    """<p>The user-provided description of the secret.</p>"""
    kms_key_id: NotRequired[
        "aws_sdk_secrets_manager.types.kms_key_id_type.KmsKeyIdType"
    ]
    """<p>The ARN of the KMS key that Secrets Manager uses to encrypt the secret value. If the secret is encrypted with the Amazon Web Services managed key <code>aws/secretsmanager</code>, this field is omitted.</p>"""
    rotation_enabled: (
        "aws_sdk_secrets_manager.types.rotation_enabled_type.RotationEnabledType"
    )
    """<p>Indicates whether automatic, scheduled rotation is enabled for this secret.</p>"""
    rotation_lambda_arn: NotRequired[
        "aws_sdk_secrets_manager.types.rotation_lambda_arn_type.RotationLambdaARNType"
    ]
    """<p>The ARN of an Amazon Web Services Lambda function invoked by Secrets Manager to rotate and expire the secret either automatically per the schedule or manually by a call to <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RotateSecret.html\"> <code>RotateSecret</code> </a>.</p>"""
    rotation_rules: NotRequired[
        "aws_sdk_secrets_manager.types.rotation_rules_type.RotationRulesType"
    ]
    """<p>A structure that defines the rotation configuration for the secret.</p>"""
    external_secret_rotation_metadata: NotRequired[
        "aws_sdk_secrets_manager.types.external_secret_rotation_metadata_type.ExternalSecretRotationMetadataType"
    ]
    """<p>The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html\">Managed external secrets partners</a>.</p>"""
    external_secret_rotation_role_arn: NotRequired[
        "aws_sdk_secrets_manager.types.role_arn_type.RoleARNType"
    ]
    """<p>The role that Secrets Manager assumes to call APIs required to perform the rotation. For more information about the required information, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-partners.html\">Managed external secrets partners</a>.</p>"""
    last_rotated_date: NotRequired[
        "aws_sdk_secrets_manager.types.last_rotated_date_type.LastRotatedDateType"
    ]
    """<p>The most recent date and time that the Secrets Manager rotation process was successfully completed. This value is null if the secret hasn't ever rotated.</p>"""
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
    """<p>The date and time the deletion of the secret occurred. Not present on active secrets. The secret can be recovered until the number of days in the recovery window has passed, as specified in the <code>RecoveryWindowInDays</code> parameter of the <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_DeleteSecret.html\"> <code>DeleteSecret</code> </a> operation.</p>"""
    next_rotation_date: NotRequired[
        "aws_sdk_secrets_manager.types.next_rotation_date_type.NextRotationDateType"
    ]
    """<p>The next rotation is scheduled to occur on or before this date. If the secret isn't configured for rotation or rotation has been disabled, Secrets Manager returns null.</p>"""
    tags: NotRequired["aws_sdk_secrets_manager.types.tag_list_type.TagListType"]
    """<p>The list of user-defined tags associated with the secret. To add tags to a secret, use <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_TagResource.html\"> <code>TagResource</code> </a>. To remove tags, use <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_UntagResource.html\"> <code>UntagResource</code> </a>.</p>"""
    secret_versions_to_stages: NotRequired[
        "aws_sdk_secrets_manager.types.secret_versions_to_stages_map_type.SecretVersionsToStagesMapType"
    ]
    """<p>A list of all of the currently assigned <code>SecretVersionStage</code> staging labels and the <code>SecretVersionId</code> attached to each one. Staging labels are used to keep track of the different versions during the rotation process.</p> <note> <p>A version that does not have any <code>SecretVersionStage</code> is considered deprecated and subject to deletion. Such versions are not included in this list.</p> </note>"""
    owning_service: NotRequired[
        "aws_sdk_secrets_manager.types.owning_service_type.OwningServiceType"
    ]
    """<p>Returns the name of the service that created the secret.</p>"""
    created_date: NotRequired[
        "aws_sdk_secrets_manager.types.timestamp_type.TimestampType"
    ]
    """<p>The date and time when a secret was created.</p>"""
    primary_region: NotRequired["aws_sdk_secrets_manager.types.region_type.RegionType"]
    """<p>The Region where Secrets Manager originated the secret.</p>"""
