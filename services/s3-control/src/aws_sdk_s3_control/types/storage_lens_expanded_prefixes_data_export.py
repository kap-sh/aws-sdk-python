"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensExpandedPrefixesDataExport``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_bucket_destination
    import aws_sdk_s3_control.types.storage_lens_table_destination


class StorageLensExpandedPrefixesDataExport(TypedDict):
    s3_bucket_destination: NotRequired[
        "aws_sdk_s3_control.types.s3_bucket_destination.S3BucketDestination"
    ]
    storage_lens_table_destination: NotRequired[
        "aws_sdk_s3_control.types.storage_lens_table_destination.StorageLensTableDestination"
    ]
    """<p>A container for the bucket where the S3 Storage Lens metric export files are located. At least one export destination must be specified.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensExpandedPrefixesDataExport, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "s3_bucket_destination" in value:
        import aws_sdk_s3_control.types.s3_bucket_destination

        aws_sdk_s3_control.types.s3_bucket_destination.serialize_xml(
            value["s3_bucket_destination"], el, "S3BucketDestination"
        )
    if "storage_lens_table_destination" in value:
        import aws_sdk_s3_control.types.storage_lens_table_destination

        aws_sdk_s3_control.types.storage_lens_table_destination.serialize_xml(
            value["storage_lens_table_destination"], el, "StorageLensTableDestination"
        )


def deserialize_xml(el: Element) -> StorageLensExpandedPrefixesDataExport:
    out: StorageLensExpandedPrefixesDataExport = {}  # type: ignore[typeddict-item]
    child_s3_bucket_destination = el.find("S3BucketDestination")
    if child_s3_bucket_destination is not None:
        import aws_sdk_s3_control.types.s3_bucket_destination

        out["s3_bucket_destination"] = (
            aws_sdk_s3_control.types.s3_bucket_destination.deserialize_xml(
                child_s3_bucket_destination
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
