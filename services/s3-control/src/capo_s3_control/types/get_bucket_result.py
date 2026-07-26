"""Generated from Smithy shape ``com.amazonaws.s3control#GetBucketResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.creation_date
    import capo_s3_control.types.public_access_block_enabled


class GetBucketResult(TypedDict, closed=True):
    bucket: NotRequired["capo_s3_control.types.bucket_name.BucketName"]
    """<p>The Outposts bucket requested.</p>"""
    public_access_block_enabled: (
        "capo_s3_control.types.public_access_block_enabled.PublicAccessBlockEnabled"
    )
    """<p></p>"""
    creation_date: NotRequired["capo_s3_control.types.creation_date.CreationDate"]
    """<p>The creation date of the Outposts bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    SubElement(el, "PublicAccessBlockEnabled").text = (
        "true" if value.get("public_access_block_enabled", False) else "false"
    )
    if "creation_date" in value:
        import capo_s3_control.types.creation_date

        capo_s3_control.types.creation_date.serialize_xml(
            value["creation_date"], el, "CreationDate"
        )


def deserialize_xml(el: Element) -> GetBucketResult:
    out: GetBucketResult = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_public_access_block_enabled = el.find("PublicAccessBlockEnabled")
    if child_public_access_block_enabled is not None:
        out["public_access_block_enabled"] = (
            child_public_access_block_enabled.text or ""
        ).lower() == "true"
    else:
        out["public_access_block_enabled"] = False
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import capo_s3_control.types.creation_date

        out["creation_date"] = capo_s3_control.types.creation_date.deserialize_xml(
            child_creation_date
        )
    return out
