"""Generated from Smithy shape ``com.amazonaws.s3#ObjectEncryption``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_s3.errors import DeserializationError, SerializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.ssekms_encryption


class _ObjectEncryption_SSEKMS(TypedDict):
    SSEKMS: "aws_sdk_s3.types.ssekms_encryption.SSEKMSEncryption"


ObjectEncryption: TypeAlias = _ObjectEncryption_SSEKMS


# --- restXml ser/de ---
def serialize_xml(value: ObjectEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "SSEKMS" in value:
        import aws_sdk_s3.types.ssekms_encryption

        aws_sdk_s3.types.ssekms_encryption.serialize_xml(value["SSEKMS"], el, "SSE-KMS")
    else:
        raise SerializationError("ObjectEncryption: no variant present")


def deserialize_xml(el: Element) -> ObjectEncryption:
    for child in el:
        if child.tag == "SSE-KMS":
            import aws_sdk_s3.types.ssekms_encryption

            return {"SSEKMS": aws_sdk_s3.types.ssekms_encryption.deserialize_xml(child)}
    raise DeserializationError("ObjectEncryption: no recognized variant element")
