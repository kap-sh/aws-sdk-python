"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Configuration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.dynamodb_stream_configuration
    import aws_sdk_accessanalyzer.types.dynamodb_table_configuration
    import aws_sdk_accessanalyzer.types.ebs_snapshot_configuration
    import aws_sdk_accessanalyzer.types.ecr_repository_configuration
    import aws_sdk_accessanalyzer.types.efs_file_system_configuration
    import aws_sdk_accessanalyzer.types.iam_role_configuration
    import aws_sdk_accessanalyzer.types.kms_key_configuration
    import aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_configuration
    import aws_sdk_accessanalyzer.types.rds_db_snapshot_configuration
    import aws_sdk_accessanalyzer.types.s3_bucket_configuration
    import aws_sdk_accessanalyzer.types.s3_express_directory_bucket_configuration
    import aws_sdk_accessanalyzer.types.secrets_manager_secret_configuration
    import aws_sdk_accessanalyzer.types.sns_topic_configuration
    import aws_sdk_accessanalyzer.types.sqs_queue_configuration


class _Configuration_ebsSnapshot(TypedDict, closed=True):
    ebsSnapshot: "aws_sdk_accessanalyzer.types.ebs_snapshot_configuration.EbsSnapshotConfiguration"


class _Configuration_ecrRepository(TypedDict, closed=True):
    ecrRepository: "aws_sdk_accessanalyzer.types.ecr_repository_configuration.EcrRepositoryConfiguration"


class _Configuration_iamRole(TypedDict, closed=True):
    iamRole: "aws_sdk_accessanalyzer.types.iam_role_configuration.IamRoleConfiguration"


class _Configuration_efsFileSystem(TypedDict, closed=True):
    efsFileSystem: "aws_sdk_accessanalyzer.types.efs_file_system_configuration.EfsFileSystemConfiguration"


class _Configuration_kmsKey(TypedDict, closed=True):
    kmsKey: "aws_sdk_accessanalyzer.types.kms_key_configuration.KmsKeyConfiguration"


class _Configuration_rdsDbClusterSnapshot(TypedDict, closed=True):
    rdsDbClusterSnapshot: "aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_configuration.RdsDbClusterSnapshotConfiguration"


class _Configuration_rdsDbSnapshot(TypedDict, closed=True):
    rdsDbSnapshot: "aws_sdk_accessanalyzer.types.rds_db_snapshot_configuration.RdsDbSnapshotConfiguration"


class _Configuration_secretsManagerSecret(TypedDict, closed=True):
    secretsManagerSecret: "aws_sdk_accessanalyzer.types.secrets_manager_secret_configuration.SecretsManagerSecretConfiguration"


class _Configuration_s3Bucket(TypedDict, closed=True):
    s3Bucket: (
        "aws_sdk_accessanalyzer.types.s3_bucket_configuration.S3BucketConfiguration"
    )


class _Configuration_snsTopic(TypedDict, closed=True):
    snsTopic: (
        "aws_sdk_accessanalyzer.types.sns_topic_configuration.SnsTopicConfiguration"
    )


class _Configuration_sqsQueue(TypedDict, closed=True):
    sqsQueue: (
        "aws_sdk_accessanalyzer.types.sqs_queue_configuration.SqsQueueConfiguration"
    )


class _Configuration_s3ExpressDirectoryBucket(TypedDict, closed=True):
    s3ExpressDirectoryBucket: "aws_sdk_accessanalyzer.types.s3_express_directory_bucket_configuration.S3ExpressDirectoryBucketConfiguration"


class _Configuration_dynamodbStream(TypedDict, closed=True):
    dynamodbStream: "aws_sdk_accessanalyzer.types.dynamodb_stream_configuration.DynamodbStreamConfiguration"


class _Configuration_dynamodbTable(TypedDict, closed=True):
    dynamodbTable: "aws_sdk_accessanalyzer.types.dynamodb_table_configuration.DynamodbTableConfiguration"


Configuration: TypeAlias = (
    _Configuration_ebsSnapshot
    | _Configuration_ecrRepository
    | _Configuration_iamRole
    | _Configuration_efsFileSystem
    | _Configuration_kmsKey
    | _Configuration_rdsDbClusterSnapshot
    | _Configuration_rdsDbSnapshot
    | _Configuration_secretsManagerSecret
    | _Configuration_s3Bucket
    | _Configuration_snsTopic
    | _Configuration_sqsQueue
    | _Configuration_s3ExpressDirectoryBucket
    | _Configuration_dynamodbStream
    | _Configuration_dynamodbTable
)


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    if "ebsSnapshot" in value:
        import aws_sdk_accessanalyzer.types.ebs_snapshot_configuration

        return {
            "ebsSnapshot": aws_sdk_accessanalyzer.types.ebs_snapshot_configuration.serialize_json(
                value["ebsSnapshot"]
            )
        }
    elif "ecrRepository" in value:
        import aws_sdk_accessanalyzer.types.ecr_repository_configuration

        return {
            "ecrRepository": aws_sdk_accessanalyzer.types.ecr_repository_configuration.serialize_json(
                value["ecrRepository"]
            )
        }
    elif "iamRole" in value:
        import aws_sdk_accessanalyzer.types.iam_role_configuration

        return {
            "iamRole": aws_sdk_accessanalyzer.types.iam_role_configuration.serialize_json(
                value["iamRole"]
            )
        }
    elif "efsFileSystem" in value:
        import aws_sdk_accessanalyzer.types.efs_file_system_configuration

        return {
            "efsFileSystem": aws_sdk_accessanalyzer.types.efs_file_system_configuration.serialize_json(
                value["efsFileSystem"]
            )
        }
    elif "kmsKey" in value:
        import aws_sdk_accessanalyzer.types.kms_key_configuration

        return {
            "kmsKey": aws_sdk_accessanalyzer.types.kms_key_configuration.serialize_json(
                value["kmsKey"]
            )
        }
    elif "rdsDbClusterSnapshot" in value:
        import aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_configuration

        return {
            "rdsDbClusterSnapshot": aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_configuration.serialize_json(
                value["rdsDbClusterSnapshot"]
            )
        }
    elif "rdsDbSnapshot" in value:
        import aws_sdk_accessanalyzer.types.rds_db_snapshot_configuration

        return {
            "rdsDbSnapshot": aws_sdk_accessanalyzer.types.rds_db_snapshot_configuration.serialize_json(
                value["rdsDbSnapshot"]
            )
        }
    elif "secretsManagerSecret" in value:
        import aws_sdk_accessanalyzer.types.secrets_manager_secret_configuration

        return {
            "secretsManagerSecret": aws_sdk_accessanalyzer.types.secrets_manager_secret_configuration.serialize_json(
                value["secretsManagerSecret"]
            )
        }
    elif "s3Bucket" in value:
        import aws_sdk_accessanalyzer.types.s3_bucket_configuration

        return {
            "s3Bucket": aws_sdk_accessanalyzer.types.s3_bucket_configuration.serialize_json(
                value["s3Bucket"]
            )
        }
    elif "snsTopic" in value:
        import aws_sdk_accessanalyzer.types.sns_topic_configuration

        return {
            "snsTopic": aws_sdk_accessanalyzer.types.sns_topic_configuration.serialize_json(
                value["snsTopic"]
            )
        }
    elif "sqsQueue" in value:
        import aws_sdk_accessanalyzer.types.sqs_queue_configuration

        return {
            "sqsQueue": aws_sdk_accessanalyzer.types.sqs_queue_configuration.serialize_json(
                value["sqsQueue"]
            )
        }
    elif "s3ExpressDirectoryBucket" in value:
        import aws_sdk_accessanalyzer.types.s3_express_directory_bucket_configuration

        return {
            "s3ExpressDirectoryBucket": aws_sdk_accessanalyzer.types.s3_express_directory_bucket_configuration.serialize_json(
                value["s3ExpressDirectoryBucket"]
            )
        }
    elif "dynamodbStream" in value:
        import aws_sdk_accessanalyzer.types.dynamodb_stream_configuration

        return {
            "dynamodbStream": aws_sdk_accessanalyzer.types.dynamodb_stream_configuration.serialize_json(
                value["dynamodbStream"]
            )
        }
    elif "dynamodbTable" in value:
        import aws_sdk_accessanalyzer.types.dynamodb_table_configuration

        return {
            "dynamodbTable": aws_sdk_accessanalyzer.types.dynamodb_table_configuration.serialize_json(
                value["dynamodbTable"]
            )
        }
    else:
        raise SerializationError("Configuration: no variant present")


def deserialize_json(data: dict) -> Configuration:
    if "ebsSnapshot" in data:
        import aws_sdk_accessanalyzer.types.ebs_snapshot_configuration

        return {
            "ebsSnapshot": aws_sdk_accessanalyzer.types.ebs_snapshot_configuration.deserialize_json(
                data["ebsSnapshot"]
            )
        }
    elif "ecrRepository" in data:
        import aws_sdk_accessanalyzer.types.ecr_repository_configuration

        return {
            "ecrRepository": aws_sdk_accessanalyzer.types.ecr_repository_configuration.deserialize_json(
                data["ecrRepository"]
            )
        }
    elif "iamRole" in data:
        import aws_sdk_accessanalyzer.types.iam_role_configuration

        return {
            "iamRole": aws_sdk_accessanalyzer.types.iam_role_configuration.deserialize_json(
                data["iamRole"]
            )
        }
    elif "efsFileSystem" in data:
        import aws_sdk_accessanalyzer.types.efs_file_system_configuration

        return {
            "efsFileSystem": aws_sdk_accessanalyzer.types.efs_file_system_configuration.deserialize_json(
                data["efsFileSystem"]
            )
        }
    elif "kmsKey" in data:
        import aws_sdk_accessanalyzer.types.kms_key_configuration

        return {
            "kmsKey": aws_sdk_accessanalyzer.types.kms_key_configuration.deserialize_json(
                data["kmsKey"]
            )
        }
    elif "rdsDbClusterSnapshot" in data:
        import aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_configuration

        return {
            "rdsDbClusterSnapshot": aws_sdk_accessanalyzer.types.rds_db_cluster_snapshot_configuration.deserialize_json(
                data["rdsDbClusterSnapshot"]
            )
        }
    elif "rdsDbSnapshot" in data:
        import aws_sdk_accessanalyzer.types.rds_db_snapshot_configuration

        return {
            "rdsDbSnapshot": aws_sdk_accessanalyzer.types.rds_db_snapshot_configuration.deserialize_json(
                data["rdsDbSnapshot"]
            )
        }
    elif "secretsManagerSecret" in data:
        import aws_sdk_accessanalyzer.types.secrets_manager_secret_configuration

        return {
            "secretsManagerSecret": aws_sdk_accessanalyzer.types.secrets_manager_secret_configuration.deserialize_json(
                data["secretsManagerSecret"]
            )
        }
    elif "s3Bucket" in data:
        import aws_sdk_accessanalyzer.types.s3_bucket_configuration

        return {
            "s3Bucket": aws_sdk_accessanalyzer.types.s3_bucket_configuration.deserialize_json(
                data["s3Bucket"]
            )
        }
    elif "snsTopic" in data:
        import aws_sdk_accessanalyzer.types.sns_topic_configuration

        return {
            "snsTopic": aws_sdk_accessanalyzer.types.sns_topic_configuration.deserialize_json(
                data["snsTopic"]
            )
        }
    elif "sqsQueue" in data:
        import aws_sdk_accessanalyzer.types.sqs_queue_configuration

        return {
            "sqsQueue": aws_sdk_accessanalyzer.types.sqs_queue_configuration.deserialize_json(
                data["sqsQueue"]
            )
        }
    elif "s3ExpressDirectoryBucket" in data:
        import aws_sdk_accessanalyzer.types.s3_express_directory_bucket_configuration

        return {
            "s3ExpressDirectoryBucket": aws_sdk_accessanalyzer.types.s3_express_directory_bucket_configuration.deserialize_json(
                data["s3ExpressDirectoryBucket"]
            )
        }
    elif "dynamodbStream" in data:
        import aws_sdk_accessanalyzer.types.dynamodb_stream_configuration

        return {
            "dynamodbStream": aws_sdk_accessanalyzer.types.dynamodb_stream_configuration.deserialize_json(
                data["dynamodbStream"]
            )
        }
    elif "dynamodbTable" in data:
        import aws_sdk_accessanalyzer.types.dynamodb_table_configuration

        return {
            "dynamodbTable": aws_sdk_accessanalyzer.types.dynamodb_table_configuration.deserialize_json(
                data["dynamodbTable"]
            )
        }
    else:
        raise DeserializationError("Configuration: no recognized variant key")
