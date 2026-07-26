"""Generated from Smithy shape ``com.amazonaws.mgn#PostLaunchActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.bounded_string
    import capo_mgn.types.cloud_watch_log_group_name
    import capo_mgn.types.post_launch_actions_deployment_type
    import capo_mgn.types.s3_log_bucket_name
    import capo_mgn.types.ssm_documents


class PostLaunchActions(TypedDict, closed=True):
    deployment: NotRequired[
        "capo_mgn.types.post_launch_actions_deployment_type.PostLaunchActionsDeploymentType"
    ]
    """<p>Deployment type in which AWS Systems Manager Documents will be executed.</p>"""
    s3_log_bucket: NotRequired["capo_mgn.types.s3_log_bucket_name.S3LogBucketName"]
    """<p>AWS Systems Manager Command's logs S3 log bucket.</p>"""
    s3_output_key_prefix: NotRequired["capo_mgn.types.bounded_string.BoundedString"]
    """<p>AWS Systems Manager Command's logs S3 output key prefix.</p>"""
    cloud_watch_log_group_name: NotRequired[
        "capo_mgn.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
    ]
    """<p>AWS Systems Manager Command's CloudWatch log group name.</p>"""
    ssm_documents: NotRequired["capo_mgn.types.ssm_documents.SsmDocuments"]
    """<p>AWS Systems Manager Documents.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PostLaunchActions) -> dict:
    out: dict = {}
    if "deployment" in value:
        out["deployment"] = value["deployment"]
    if "s3_log_bucket" in value:
        out["s3LogBucket"] = value["s3_log_bucket"]
    if "s3_output_key_prefix" in value:
        out["s3OutputKeyPrefix"] = value["s3_output_key_prefix"]
    if "cloud_watch_log_group_name" in value:
        out["cloudWatchLogGroupName"] = value["cloud_watch_log_group_name"]
    if "ssm_documents" in value:
        import capo_mgn.types.ssm_documents

        out["ssmDocuments"] = capo_mgn.types.ssm_documents.serialize_json(
            value["ssm_documents"]
        )
    return out


def deserialize_json(data: dict) -> PostLaunchActions:
    out: PostLaunchActions = {}  # type: ignore[typeddict-item]
    if "deployment" in data:
        out["deployment"] = data["deployment"]
    if "s3LogBucket" in data:
        out["s3_log_bucket"] = data["s3LogBucket"]
    if "s3OutputKeyPrefix" in data:
        out["s3_output_key_prefix"] = data["s3OutputKeyPrefix"]
    if "cloudWatchLogGroupName" in data:
        out["cloud_watch_log_group_name"] = data["cloudWatchLogGroupName"]
    if "ssmDocuments" in data:
        import capo_mgn.types.ssm_documents

        out["ssm_documents"] = capo_mgn.types.ssm_documents.deserialize_json(
            data["ssmDocuments"]
        )
    return out
