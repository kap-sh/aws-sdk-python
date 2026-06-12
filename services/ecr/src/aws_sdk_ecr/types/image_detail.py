"""Generated from Smithy shape ``com.amazonaws.ecr#ImageDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_digest
    import aws_sdk_ecr.types.image_scan_findings_summary
    import aws_sdk_ecr.types.image_scan_status
    import aws_sdk_ecr.types.image_size_in_bytes
    import aws_sdk_ecr.types.image_status
    import aws_sdk_ecr.types.image_tag_list
    import aws_sdk_ecr.types.last_activated_at_timestamp
    import aws_sdk_ecr.types.last_archived_at_timestamp
    import aws_sdk_ecr.types.media_type
    import aws_sdk_ecr.types.push_timestamp
    import aws_sdk_ecr.types.recorded_pull_timestamp
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class ImageDetail(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to which this image belongs.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository to which this image belongs.</p>"""
    image_digest: NotRequired["aws_sdk_ecr.types.image_digest.ImageDigest"]
    """<p>The <code>sha256</code> digest of the image manifest.</p>"""
    image_tags: NotRequired["aws_sdk_ecr.types.image_tag_list.ImageTagList"]
    """<p>The list of tags associated with this image.</p>"""
    image_size_in_bytes: NotRequired[
        "aws_sdk_ecr.types.image_size_in_bytes.ImageSizeInBytes"
    ]
    """<p>The size, in bytes, of the image in the repository.</p> <p>If the image is a manifest list, this will be the max size of all manifests in the list.</p> <note> <p>Starting with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the <code>docker images</code> command shows the uncompressed image size. Therefore, Docker might return a larger image than the image shown in the Amazon Web Services Management Console.</p> </note>"""
    image_pushed_at: NotRequired["aws_sdk_ecr.types.push_timestamp.PushTimestamp"]
    """<p>The date and time, expressed in standard JavaScript date format, at which the current image was pushed to the repository. </p>"""
    image_scan_status: NotRequired[
        "aws_sdk_ecr.types.image_scan_status.ImageScanStatus"
    ]
    """<p>The current state of the scan.</p>"""
    image_scan_findings_summary: NotRequired[
        "aws_sdk_ecr.types.image_scan_findings_summary.ImageScanFindingsSummary"
    ]
    """<p>A summary of the last completed image scan.</p>"""
    image_manifest_media_type: NotRequired["aws_sdk_ecr.types.media_type.MediaType"]
    """<p>The media type of the image manifest.</p>"""
    artifact_media_type: NotRequired["aws_sdk_ecr.types.media_type.MediaType"]
    """<p>The artifact media type of the image.</p>"""
    last_recorded_pull_time: NotRequired[
        "aws_sdk_ecr.types.recorded_pull_timestamp.RecordedPullTimestamp"
    ]
    """<p>The date and time, expressed in standard JavaScript date format, when Amazon ECR recorded the last image pull.</p> <note> <p>Amazon ECR refreshes the last image pull timestamp at least once every 24 hours. For example, if you pull an image once a day then the <code>lastRecordedPullTime</code> timestamp will indicate the exact time that the image was last pulled. However, if you pull an image once an hour, because Amazon ECR refreshes the <code>lastRecordedPullTime</code> timestamp at least once every 24 hours, the result may not be the exact time that the image was last pulled.</p> </note>"""
    subject_manifest_digest: NotRequired["aws_sdk_ecr.types.image_digest.ImageDigest"]
    """<p>The digest of the subject manifest for images that are referrers.</p>"""
    image_status: NotRequired["aws_sdk_ecr.types.image_status.ImageStatus"]
    """<p>The current status of the image.</p>"""
    last_archived_at: NotRequired[
        "aws_sdk_ecr.types.last_archived_at_timestamp.LastArchivedAtTimestamp"
    ]
    """<p>The date and time, expressed in standard JavaScript date format, when the image was last transitioned to Amazon ECR archive.</p>"""
    last_activated_at: NotRequired[
        "aws_sdk_ecr.types.last_activated_at_timestamp.LastActivatedAtTimestamp"
    ]
    """<p>The date and time, expressed in standard JavaScript date format, when the image was last restored from Amazon ECR archive to Amazon ECR standard.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageDetail) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_digest" in value:
        out["imageDigest"] = value["image_digest"]
    if "image_tags" in value:
        import aws_sdk_ecr.types.image_tag_list

        out["imageTags"] = aws_sdk_ecr.types.image_tag_list.serialize_aws_json_1_1(
            value["image_tags"]
        )
    if "image_size_in_bytes" in value:
        out["imageSizeInBytes"] = value["image_size_in_bytes"]
    if "image_pushed_at" in value:
        import aws_sdk_ecr.types.push_timestamp

        out["imagePushedAt"] = aws_sdk_ecr.types.push_timestamp.serialize_aws_json_1_1(
            value["image_pushed_at"]
        )
    if "image_scan_status" in value:
        import aws_sdk_ecr.types.image_scan_status

        out["imageScanStatus"] = (
            aws_sdk_ecr.types.image_scan_status.serialize_aws_json_1_1(
                value["image_scan_status"]
            )
        )
    if "image_scan_findings_summary" in value:
        import aws_sdk_ecr.types.image_scan_findings_summary

        out["imageScanFindingsSummary"] = (
            aws_sdk_ecr.types.image_scan_findings_summary.serialize_aws_json_1_1(
                value["image_scan_findings_summary"]
            )
        )
    if "image_manifest_media_type" in value:
        out["imageManifestMediaType"] = value["image_manifest_media_type"]
    if "artifact_media_type" in value:
        out["artifactMediaType"] = value["artifact_media_type"]
    if "last_recorded_pull_time" in value:
        import aws_sdk_ecr.types.recorded_pull_timestamp

        out["lastRecordedPullTime"] = (
            aws_sdk_ecr.types.recorded_pull_timestamp.serialize_aws_json_1_1(
                value["last_recorded_pull_time"]
            )
        )
    if "subject_manifest_digest" in value:
        out["subjectManifestDigest"] = value["subject_manifest_digest"]
    if "image_status" in value:
        import aws_sdk_ecr.types.image_status

        out["imageStatus"] = aws_sdk_ecr.types.image_status.serialize_aws_json_1_1(
            value["image_status"]
        )
    if "last_archived_at" in value:
        import aws_sdk_ecr.types.last_archived_at_timestamp

        out["lastArchivedAt"] = (
            aws_sdk_ecr.types.last_archived_at_timestamp.serialize_aws_json_1_1(
                value["last_archived_at"]
            )
        )
    if "last_activated_at" in value:
        import aws_sdk_ecr.types.last_activated_at_timestamp

        out["lastActivatedAt"] = (
            aws_sdk_ecr.types.last_activated_at_timestamp.serialize_aws_json_1_1(
                value["last_activated_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageDetail:
    out: ImageDetail = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "imageDigest" in data:
        out["image_digest"] = data["imageDigest"]
    if "imageTags" in data:
        import aws_sdk_ecr.types.image_tag_list

        out["image_tags"] = aws_sdk_ecr.types.image_tag_list.deserialize_aws_json_1_1(
            data["imageTags"]
        )
    if "imageSizeInBytes" in data:
        out["image_size_in_bytes"] = data["imageSizeInBytes"]
    if "imagePushedAt" in data:
        import aws_sdk_ecr.types.push_timestamp

        out["image_pushed_at"] = (
            aws_sdk_ecr.types.push_timestamp.deserialize_aws_json_1_1(
                data["imagePushedAt"]
            )
        )
    if "imageScanStatus" in data:
        import aws_sdk_ecr.types.image_scan_status

        out["image_scan_status"] = (
            aws_sdk_ecr.types.image_scan_status.deserialize_aws_json_1_1(
                data["imageScanStatus"]
            )
        )
    if "imageScanFindingsSummary" in data:
        import aws_sdk_ecr.types.image_scan_findings_summary

        out["image_scan_findings_summary"] = (
            aws_sdk_ecr.types.image_scan_findings_summary.deserialize_aws_json_1_1(
                data["imageScanFindingsSummary"]
            )
        )
    if "imageManifestMediaType" in data:
        out["image_manifest_media_type"] = data["imageManifestMediaType"]
    if "artifactMediaType" in data:
        out["artifact_media_type"] = data["artifactMediaType"]
    if "lastRecordedPullTime" in data:
        import aws_sdk_ecr.types.recorded_pull_timestamp

        out["last_recorded_pull_time"] = (
            aws_sdk_ecr.types.recorded_pull_timestamp.deserialize_aws_json_1_1(
                data["lastRecordedPullTime"]
            )
        )
    if "subjectManifestDigest" in data:
        out["subject_manifest_digest"] = data["subjectManifestDigest"]
    if "imageStatus" in data:
        import aws_sdk_ecr.types.image_status

        out["image_status"] = aws_sdk_ecr.types.image_status.deserialize_aws_json_1_1(
            data["imageStatus"]
        )
    if "lastArchivedAt" in data:
        import aws_sdk_ecr.types.last_archived_at_timestamp

        out["last_archived_at"] = (
            aws_sdk_ecr.types.last_archived_at_timestamp.deserialize_aws_json_1_1(
                data["lastArchivedAt"]
            )
        )
    if "lastActivatedAt" in data:
        import aws_sdk_ecr.types.last_activated_at_timestamp

        out["last_activated_at"] = (
            aws_sdk_ecr.types.last_activated_at_timestamp.deserialize_aws_json_1_1(
                data["lastActivatedAt"]
            )
        )
    return out
