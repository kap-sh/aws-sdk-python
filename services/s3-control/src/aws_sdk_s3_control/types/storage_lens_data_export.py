"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensDataExport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.cloud_watch_metrics
    import aws_sdk_s3_control.types.s3_bucket_destination
    import aws_sdk_s3_control.types.storage_lens_table_destination


class StorageLensDataExport(TypedDict):
    s3_bucket_destination: NotRequired[
        "aws_sdk_s3_control.types.s3_bucket_destination.S3BucketDestination"
    ]
    """<p>A container for the bucket where the S3 Storage Lens metrics export will be located.</p> <note> <p>This bucket must be located in the same Region as the storage lens configuration. </p> </note>"""
    cloud_watch_metrics: NotRequired[
        "aws_sdk_s3_control.types.cloud_watch_metrics.CloudWatchMetrics"
    ]
    """<p>A container for enabling Amazon CloudWatch publishing for S3 Storage Lens metrics.</p>"""
    storage_lens_table_destination: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_table_destination.StorageLensTableDestination"
    ]
    """<p>A container for configuring S3 Storage Lens data exports to read-only S3 table buckets.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StorageLensDataExport, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "s3_bucket_destination" in value:
        import aws_sdk_s3_control.types.s3_bucket_destination

        aws_sdk_s3_control.types.s3_bucket_destination.serialize_xml(
            value["s3_bucket_destination"], el, "S3BucketDestination"
        )
    if "cloud_watch_metrics" in value:
        import aws_sdk_s3_control.types.cloud_watch_metrics

        aws_sdk_s3_control.types.cloud_watch_metrics.serialize_xml(
            value["cloud_watch_metrics"], el, "CloudWatchMetrics"
        )
    if "storage_lens_table_destination" in value:
        import aws_sdk_s3_control.types.storage_lens_table_destination

        aws_sdk_s3_control.types.storage_lens_table_destination.serialize_xml(
            value["storage_lens_table_destination"], el, "StorageLensTableDestination"
        )


def deserialize_xml(el: Element) -> StorageLensDataExport:
    out: StorageLensDataExport = {}  # type: ignore[typeddict-item]
    child_s3_bucket_destination = el.find("S3BucketDestination")
    if child_s3_bucket_destination is not None:
        import aws_sdk_s3_control.types.s3_bucket_destination

        out["s3_bucket_destination"] = (
            aws_sdk_s3_control.types.s3_bucket_destination.deserialize_xml(
                child_s3_bucket_destination
            )
        )
    child_cloud_watch_metrics = el.find("CloudWatchMetrics")
    if child_cloud_watch_metrics is not None:
        import aws_sdk_s3_control.types.cloud_watch_metrics

        out["cloud_watch_metrics"] = (
            aws_sdk_s3_control.types.cloud_watch_metrics.deserialize_xml(
                child_cloud_watch_metrics
            )
        )
    child_storage_lens_table_destination = el.find("StorageLensTableDestination")
    if child_storage_lens_table_destination is not None:
        import aws_sdk_s3_control.types.storage_lens_table_destination

        out["storage_lens_table_destination"] = (
            aws_sdk_s3_control.types.storage_lens_table_destination.deserialize_xml(
                child_storage_lens_table_destination
            )
        )
    return out
