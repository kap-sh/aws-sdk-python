"""Generated from Smithy shape ``com.amazonaws.s3control#S3UpdateObjectEncryptionOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.object_encryption


class S3UpdateObjectEncryptionOperation(TypedDict, closed=True):
    object_encryption: NotRequired[
        "capo_s3_control.types.object_encryption.ObjectEncryption"
    ]
    """<p>The updated server-side encryption type for this S3 object. The <code>UpdateObjectEncryption</code> operation supports the SSE-KMS encryption type.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: S3UpdateObjectEncryptionOperation, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "object_encryption" in value:
        import capo_s3_control.types.object_encryption

        capo_s3_control.types.object_encryption.serialize_xml(
            value["object_encryption"], el, "ObjectEncryption"
        )


def deserialize_xml(el: Element) -> S3UpdateObjectEncryptionOperation:
    out: S3UpdateObjectEncryptionOperation = {}  # type: ignore[typeddict-item]
    child_object_encryption = el.find("ObjectEncryption")
    if child_object_encryption is not None:
        import capo_s3_control.types.object_encryption

        out["object_encryption"] = (
            capo_s3_control.types.object_encryption.deserialize_xml(
                child_object_encryption
            )
        )
    return out
