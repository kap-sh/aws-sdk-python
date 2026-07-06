"""Generated from Smithy shape ``com.amazonaws.ec2#StorageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class StorageLocation(TypedDict, closed=True):
    bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the S3 bucket.</p>"""
    key: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The key.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StorageLocation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "bucket" in value:
        pairs.append((f"{prefix}.Bucket", str(value["bucket"])))
    if "key" in value:
        pairs.append((f"{prefix}.Key", str(value["key"])))


def deserialize_ec2_query(el: Element) -> StorageLocation:
    out: StorageLocation = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    return out
