"""Generated from Smithy shape ``com.amazonaws.s3#UpdateBucketMetadataInventoryTableConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.account_id
    import aws_sdk_s3.types.bucket_name
    import aws_sdk_s3.types.checksum_algorithm
    import aws_sdk_s3.types.content_md5
    import aws_sdk_s3.types.inventory_table_configuration_updates


class UpdateBucketMetadataInventoryTableConfigurationRequest(TypedDict):
    bucket: "aws_sdk_s3.types.bucket_name.BucketName"
    """<p> The general purpose bucket that corresponds to the metadata configuration that you want to enable or disable an inventory table for. </p>"""
    content_md5: NotRequired["aws_sdk_s3.types.content_md5.ContentMD5"]
    """<p> The <code>Content-MD5</code> header for the inventory table configuration. </p>"""
    checksum_algorithm: NotRequired[
        "aws_sdk_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p> The checksum algorithm to use with your inventory table configuration. </p>"""
    inventory_table_configuration: "aws_sdk_s3.types.inventory_table_configuration_updates.InventoryTableConfigurationUpdates"
    """<p> The contents of your inventory table configuration. </p>"""
    expected_bucket_owner: NotRequired["aws_sdk_s3.types.account_id.AccountId"]
    """<p> The expected owner of the general purpose bucket that corresponds to the metadata table configuration that you want to enable or disable an inventory table for. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateBucketMetadataInventoryTableConfigurationRequest,
    parent: Element,
    tag: str,
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.inventory_table_configuration_updates

    aws_sdk_s3.types.inventory_table_configuration_updates.serialize_xml(
        value["inventory_table_configuration"], el, "InventoryTableConfiguration"
    )


def deserialize_xml(
    el: Element,
) -> UpdateBucketMetadataInventoryTableConfigurationRequest:
    out: UpdateBucketMetadataInventoryTableConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_inventory_table_configuration = el.find("InventoryTableConfiguration")
    if child_inventory_table_configuration is not None:
        import aws_sdk_s3.types.inventory_table_configuration_updates

        out["inventory_table_configuration"] = (
            aws_sdk_s3.types.inventory_table_configuration_updates.deserialize_xml(
                child_inventory_table_configuration
            )
        )
    else:
        raise DeserializationError(
            "UpdateBucketMetadataInventoryTableConfigurationRequest.inventory_table_configuration required"
        )
    return out
