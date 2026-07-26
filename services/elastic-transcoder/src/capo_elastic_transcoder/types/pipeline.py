"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Pipeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.bucket_name
    import capo_elastic_transcoder.types.id
    import capo_elastic_transcoder.types.key_arn
    import capo_elastic_transcoder.types.name
    import capo_elastic_transcoder.types.notifications
    import capo_elastic_transcoder.types.pipeline_output_config
    import capo_elastic_transcoder.types.pipeline_status
    import capo_elastic_transcoder.types.role
    import capo_elastic_transcoder.types.string


class Pipeline(TypedDict, closed=True):
    id: NotRequired["capo_elastic_transcoder.types.id.Id"]
    """<p>The identifier for the pipeline. You use this value to identify the pipeline in which you want to perform a variety of operations, such as creating a job or a preset.</p>"""
    arn: NotRequired["capo_elastic_transcoder.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the pipeline.</p>"""
    name: NotRequired["capo_elastic_transcoder.types.name.Name"]
    """<p>The name of the pipeline. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.</p> <p>Constraints: Maximum 40 characters</p>"""
    status: NotRequired["capo_elastic_transcoder.types.pipeline_status.PipelineStatus"]
    """<p>The current status of the pipeline:</p> <ul> <li> <p> <code>Active</code>: The pipeline is processing jobs.</p> </li> <li> <p> <code>Paused</code>: The pipeline is not currently processing jobs.</p> </li> </ul>"""
    input_bucket: NotRequired["capo_elastic_transcoder.types.bucket_name.BucketName"]
    """<p>The Amazon S3 bucket from which Elastic Transcoder gets media files for transcoding and the graphics files, if any, that you want to use for watermarks.</p>"""
    output_bucket: NotRequired["capo_elastic_transcoder.types.bucket_name.BucketName"]
    """<p>The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files, thumbnails, and playlists. Either you specify this value, or you specify both <code>ContentConfig</code> and <code>ThumbnailConfig</code>.</p>"""
    role: NotRequired["capo_elastic_transcoder.types.role.Role"]
    """<p>The IAM Amazon Resource Name (ARN) for the role that Elastic Transcoder uses to transcode jobs for this pipeline.</p>"""
    aws_kms_key_arn: NotRequired["capo_elastic_transcoder.types.key_arn.KeyArn"]
    """<p>The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.</p> <p>If you use either <code>s3</code> or <code>s3-aws-kms</code> as your <code>Encryption:Mode</code>, you don't need to provide a key with your job because a default key, known as an AWS-KMS key, is created for you automatically. You need to provide an AWS-KMS key only if you want to use a non-default AWS-KMS key, or if you are using an <code>Encryption:Mode</code> of <code>aes-cbc-pkcs7</code>, <code>aes-ctr</code>, or <code>aes-gcm</code>.</p>"""
    notifications: NotRequired[
        "capo_elastic_transcoder.types.notifications.Notifications"
    ]
    """<p>The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.</p> <important> <p>To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.</p> </important> <ul> <li> <p> <b>Progressing</b> (optional): The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.</p> </li> <li> <p> <b>Complete</b> (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.</p> </li> <li> <p> <b>Warning</b> (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.</p> </li> <li> <p> <b>Error</b> (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.</p> </li> </ul>"""
    content_config: NotRequired[
        "capo_elastic_transcoder.types.pipeline_output_config.PipelineOutputConfig"
    ]
    """<p>Information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. Either you specify both <code>ContentConfig</code> and <code>ThumbnailConfig</code>, or you specify <code>OutputBucket</code>.</p> <ul> <li> <p> <b>Bucket</b>: The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.</p> </li> <li> <p> <b>Permissions</b>: A list of the users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access that you want them to have. </p> <ul> <li> <p>GranteeType: The type of value that appears in the <code>Grantee</code> object: </p> <ul> <li> <p> <code>Canonical</code>: Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.</p> </li> <li> <p> <code>Email</code>: The registered email address of an AWS account.</p> </li> <li> <p> <code>Group</code>: One of the following predefined Amazon S3 groups: <code>AllUsers</code>, <code>AuthenticatedUsers</code>, or <code>LogDelivery</code>.</p> </li> </ul> </li> <li> <p> <code>Grantee</code>: The AWS user or group that you want to have access to transcoded files and playlists.</p> </li> <li> <p> <code>Access</code>: The permission that you want to give to the AWS user that is listed in <code>Grantee</code>. Valid values include:</p> <ul> <li> <p> <code>READ</code>: The grantee can read the objects and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>READ_ACP</code>: The grantee can read the object ACL for objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>WRITE_ACP</code>: The grantee can write the ACL for the objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>FULL_CONTROL</code>: The grantee has <code>READ</code>, <code>READ_ACP</code>, and <code>WRITE_ACP</code> permissions for the objects that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> </ul> </li> </ul> </li> <li> <p> <b>StorageClass</b>: The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket. </p> </li> </ul>"""
    thumbnail_config: NotRequired[
        "capo_elastic_transcoder.types.pipeline_output_config.PipelineOutputConfig"
    ]
    """<p>Information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. Either you specify both <code>ContentConfig</code> and <code>ThumbnailConfig</code>, or you specify <code>OutputBucket</code>.</p> <ul> <li> <p> <code>Bucket</code>: The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. </p> </li> <li> <p> <code>Permissions</code>: A list of the users and/or predefined Amazon S3 groups you want to have access to thumbnail files, and the type of access that you want them to have. </p> <ul> <li> <p>GranteeType: The type of value that appears in the Grantee object:</p> <ul> <li> <p> <code>Canonical</code>: Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.</p> <important> <p>A canonical user ID is not the same as an AWS account number.</p> </important> </li> <li> <p> <code>Email</code>: The registered email address of an AWS account.</p> </li> <li> <p> <code>Group</code>: One of the following predefined Amazon S3 groups: <code>AllUsers</code>, <code>AuthenticatedUsers</code>, or <code>LogDelivery</code>.</p> </li> </ul> </li> <li> <p> <code>Grantee</code>: The AWS user or group that you want to have access to thumbnail files.</p> </li> <li> <p>Access: The permission that you want to give to the AWS user that is listed in Grantee. Valid values include: </p> <ul> <li> <p> <code>READ</code>: The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>READ_ACP</code>: The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>WRITE_ACP</code>: The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>FULL_CONTROL</code>: The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> </ul> </li> </ul> </li> <li> <p> <code>StorageClass</code>: The Amazon S3 storage class, <code>Standard</code> or <code>ReducedRedundancy</code>, that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Pipeline) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "input_bucket" in value:
        out["InputBucket"] = value["input_bucket"]
    if "output_bucket" in value:
        out["OutputBucket"] = value["output_bucket"]
    if "role" in value:
        out["Role"] = value["role"]
    if "aws_kms_key_arn" in value:
        out["AwsKmsKeyArn"] = value["aws_kms_key_arn"]
    if "notifications" in value:
        import capo_elastic_transcoder.types.notifications

        out["Notifications"] = (
            capo_elastic_transcoder.types.notifications.serialize_json(
                value["notifications"]
            )
        )
    if "content_config" in value:
        import capo_elastic_transcoder.types.pipeline_output_config

        out["ContentConfig"] = (
            capo_elastic_transcoder.types.pipeline_output_config.serialize_json(
                value["content_config"]
            )
        )
    if "thumbnail_config" in value:
        import capo_elastic_transcoder.types.pipeline_output_config

        out["ThumbnailConfig"] = (
            capo_elastic_transcoder.types.pipeline_output_config.serialize_json(
                value["thumbnail_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Pipeline:
    out: Pipeline = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "InputBucket" in data:
        out["input_bucket"] = data["InputBucket"]
    if "OutputBucket" in data:
        out["output_bucket"] = data["OutputBucket"]
    if "Role" in data:
        out["role"] = data["Role"]
    if "AwsKmsKeyArn" in data:
        out["aws_kms_key_arn"] = data["AwsKmsKeyArn"]
    if "Notifications" in data:
        import capo_elastic_transcoder.types.notifications

        out["notifications"] = (
            capo_elastic_transcoder.types.notifications.deserialize_json(
                data["Notifications"]
            )
        )
    if "ContentConfig" in data:
        import capo_elastic_transcoder.types.pipeline_output_config

        out["content_config"] = (
            capo_elastic_transcoder.types.pipeline_output_config.deserialize_json(
                data["ContentConfig"]
            )
        )
    if "ThumbnailConfig" in data:
        import capo_elastic_transcoder.types.pipeline_output_config

        out["thumbnail_config"] = (
            capo_elastic_transcoder.types.pipeline_output_config.deserialize_json(
                data["ThumbnailConfig"]
            )
        )
    return out
