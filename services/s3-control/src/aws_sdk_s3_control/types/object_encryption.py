"""Generated from Smithy shape ``com.amazonaws.s3control#ObjectEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.s3_update_object_encryption_ssekms


class ObjectEncryption(TypedDict, closed=True):
    ssekms: NotRequired[
        "aws_sdk_s3_control.types.s3_update_object_encryption_ssekms.S3UpdateObjectEncryptionSSEKMS"
    ]
    """<p>Specifies to update the object encryption type to server-side encryption with Key Management Service (KMS) keys (SSE-KMS).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "ssekms" in value:
        import aws_sdk_s3_control.types.s3_update_object_encryption_ssekms

        aws_sdk_s3_control.types.s3_update_object_encryption_ssekms.serialize_xml(
            value["ssekms"], el, "SSE-KMS"
        )


def deserialize_xml(el: Element) -> ObjectEncryption:
    out: ObjectEncryption = {}  # type: ignore[typeddict-item]
    child_ssekms = el.find("SSE-KMS")
    if child_ssekms is not None:
        import aws_sdk_s3_control.types.s3_update_object_encryption_ssekms

        out["ssekms"] = (
            aws_sdk_s3_control.types.s3_update_object_encryption_ssekms.deserialize_xml(
                child_ssekms
            )
        )
    return out
