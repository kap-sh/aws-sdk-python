"""Generated from Smithy shape ``com.amazonaws.s3#DeleteMarkerEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.is_latest
    import aws_sdk_s3.types.last_modified
    import aws_sdk_s3.types.object_key
    import aws_sdk_s3.types.object_version_id
    import aws_sdk_s3.types.owner


class DeleteMarkerEntry(TypedDict, closed=True):
    owner: NotRequired["aws_sdk_s3.types.owner.Owner"]
    """<p>The account that created the delete marker. </p>"""
    key: NotRequired["aws_sdk_s3.types.object_key.ObjectKey"]
    """<p>The object key.</p>"""
    version_id: NotRequired["aws_sdk_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID of an object.</p>"""
    is_latest: NotRequired["aws_sdk_s3.types.is_latest.IsLatest"]
    """<p>Specifies whether the object is (true) or is not (false) the latest version of an object. </p>"""
    last_modified: NotRequired["aws_sdk_s3.types.last_modified.LastModified"]
    """<p>Date and time when the object was last modified.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteMarkerEntry, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "owner" in value:
        import aws_sdk_s3.types.owner

        aws_sdk_s3.types.owner.serialize_xml(value["owner"], el, "Owner")
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "version_id" in value:
        SubElement(el, "VersionId").text = str(value["version_id"])
    if "is_latest" in value:
        SubElement(el, "IsLatest").text = "true" if value["is_latest"] else "false"
    if "last_modified" in value:
        import aws_sdk_s3.types.last_modified

        aws_sdk_s3.types.last_modified.serialize_xml(
            value["last_modified"], el, "LastModified"
        )


def deserialize_xml(el: Element) -> DeleteMarkerEntry:
    out: DeleteMarkerEntry = {}  # type: ignore[typeddict-item]
    child_owner = el.find("Owner")
    if child_owner is not None:
        import aws_sdk_s3.types.owner

        out["owner"] = aws_sdk_s3.types.owner.deserialize_xml(child_owner)
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    child_is_latest = el.find("IsLatest")
    if child_is_latest is not None:
        out["is_latest"] = (child_is_latest.text or "").lower() == "true"
    child_last_modified = el.find("LastModified")
    if child_last_modified is not None:
        import aws_sdk_s3.types.last_modified

        out["last_modified"] = aws_sdk_s3.types.last_modified.deserialize_xml(
            child_last_modified
        )
    return out
