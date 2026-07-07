"""Generated from Smithy shape ``com.amazonaws.s3#InventoryDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.inventory_s3_bucket_destination


class InventoryDestination(TypedDict, closed=True):
    s3_bucket_destination: (
        "aws_sdk_s3.types.inventory_s3_bucket_destination.InventoryS3BucketDestination"
    )
    """<p>Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where inventory results are published.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InventoryDestination, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.inventory_s3_bucket_destination

    aws_sdk_s3.types.inventory_s3_bucket_destination.serialize_xml(
        value["s3_bucket_destination"], el, "S3BucketDestination"
    )


def deserialize_xml(el: Element) -> InventoryDestination:
    out: InventoryDestination = {}  # type: ignore[typeddict-item]
    child_s3_bucket_destination = el.find("S3BucketDestination")
    if child_s3_bucket_destination is not None:
        import aws_sdk_s3.types.inventory_s3_bucket_destination

        out["s3_bucket_destination"] = (
            aws_sdk_s3.types.inventory_s3_bucket_destination.deserialize_xml(
                child_s3_bucket_destination
            )
        )
    else:
        raise DeserializationError(
            "InventoryDestination.s3_bucket_destination required"
        )
    return out
