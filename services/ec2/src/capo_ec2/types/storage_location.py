"""Generated from Smithy shape ``com.amazonaws.ec2#StorageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class StorageLocation(TypedDict, closed=True):
    bucket: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the S3 bucket.</p>"""
    key: NotRequired["capo_ec2.types.string.String"]
    """<p>The key.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: StorageLocation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "bucket" in value:
        pairs.append((f"{key_prefix}Bucket", str(value["bucket"])))
    if "key" in value:
        pairs.append((f"{key_prefix}Key", str(value["key"])))


def deserialize_ec2_query(el: Element) -> StorageLocation:
    out: StorageLocation = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    return out
