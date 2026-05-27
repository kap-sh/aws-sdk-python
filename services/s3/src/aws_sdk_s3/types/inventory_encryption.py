"""Generated from Smithy shape ``com.amazonaws.s3#InventoryEncryption``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.ssekms
    import aws_sdk_s3.types.sses3


class InventoryEncryption(TypedDict):
    sses3: NotRequired["aws_sdk_s3.types.sses3.SSES3"]
    """<p>Specifies the use of SSE-S3 to encrypt delivered inventory reports.</p>"""
    ssekms: NotRequired["aws_sdk_s3.types.ssekms.SSEKMS"]
    """<p>Specifies the use of SSE-KMS to encrypt delivered inventory reports.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InventoryEncryption, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "sses3" in value:
        import aws_sdk_s3.types.sses3

        aws_sdk_s3.types.sses3.serialize_xml(value["sses3"], el, "SSE-S3")
    if "ssekms" in value:
        import aws_sdk_s3.types.ssekms

        aws_sdk_s3.types.ssekms.serialize_xml(value["ssekms"], el, "SSE-KMS")


def deserialize_xml(el: Element) -> InventoryEncryption:
    out: InventoryEncryption = {}  # type: ignore[typeddict-item]
    child_sses3 = el.find("SSE-S3")
    if child_sses3 is not None:
        import aws_sdk_s3.types.sses3

        out["sses3"] = aws_sdk_s3.types.sses3.deserialize_xml(child_sses3)
    child_ssekms = el.find("SSE-KMS")
    if child_ssekms is not None:
        import aws_sdk_s3.types.ssekms

        out["ssekms"] = aws_sdk_s3.types.ssekms.deserialize_xml(child_ssekms)
    return out
