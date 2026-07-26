"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#PipelineOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elastic_transcoder.types.bucket_name
    import capo_elastic_transcoder.types.permissions
    import capo_elastic_transcoder.types.storage_class


class PipelineOutputConfig(TypedDict, closed=True):
    bucket: NotRequired["capo_elastic_transcoder.types.bucket_name.BucketName"]
    """<p> The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. Specify this value when all of the following are true:</p> <ul> <li> <p>You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.</p> </li> <li> <p>You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.</p> </li> <li> <p>You do not want to specify the permissions that Elastic Transcoder grants to the files.</p> </li> <li> <p>You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.</p> </li> </ul> <p>If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit OutputBucket and specify values for <code>ContentConfig</code> and <code>ThumbnailConfig</code> instead. </p>"""
    storage_class: NotRequired[
        "capo_elastic_transcoder.types.storage_class.StorageClass"
    ]
    """<p> The Amazon S3 storage class, <code>Standard</code> or <code>ReducedRedundancy</code>, that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket. </p>"""
    permissions: NotRequired["capo_elastic_transcoder.types.permissions.Permissions"]
    """<p>Optional. The <code>Permissions</code> object specifies which users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.</p> <p>If you include <code>Permissions</code>, Elastic Transcoder grants only the permissions that you specify. It does not grant full permissions to the owner of the role specified by <code>Role</code>. If you want that user to have full control, you must explicitly grant full control to the user.</p> <p> If you omit <code>Permissions</code>, Elastic Transcoder grants full control over the transcoded files and playlists to the owner of the role specified by <code>Role</code>, and grants no other permissions to any other user or group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineOutputConfig) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "storage_class" in value:
        out["StorageClass"] = value["storage_class"]
    if "permissions" in value:
        import capo_elastic_transcoder.types.permissions

        out["Permissions"] = capo_elastic_transcoder.types.permissions.serialize_json(
            value["permissions"]
        )
    return out


def deserialize_json(data: dict) -> PipelineOutputConfig:
    out: PipelineOutputConfig = {}  # type: ignore[typeddict-item]
    if "Bucket" in data:
        out["bucket"] = data["Bucket"]
    if "StorageClass" in data:
        out["storage_class"] = data["StorageClass"]
    if "Permissions" in data:
        import capo_elastic_transcoder.types.permissions

        out["permissions"] = capo_elastic_transcoder.types.permissions.deserialize_json(
            data["Permissions"]
        )
    return out
