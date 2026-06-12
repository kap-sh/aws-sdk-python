"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensDataExportEncryption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.ssekms
    import aws_sdk_s3_control.types.sses3


class StorageLensDataExportEncryption(TypedDict):
    sses3: NotRequired["aws_sdk_s3_control.types.sses3.SSES3"]
    """<p></p>"""
    ssekms: NotRequired["aws_sdk_s3_control.types.ssekms.SSEKMS"]
    """<p></p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensDataExportEncryption, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "sses3" in value:
        import aws_sdk_s3_control.types.sses3

        aws_sdk_s3_control.types.sses3.serialize_xml(value["sses3"], el, "SSE-S3")
    if "ssekms" in value:
        import aws_sdk_s3_control.types.ssekms

        aws_sdk_s3_control.types.ssekms.serialize_xml(value["ssekms"], el, "SSE-KMS")


def deserialize_xml(el: Element) -> StorageLensDataExportEncryption:
    out: StorageLensDataExportEncryption = {}  # type: ignore[typeddict-item]
    child_sses3 = el.find("SSE-S3")
    if child_sses3 is not None:
        import aws_sdk_s3_control.types.sses3

        out["sses3"] = aws_sdk_s3_control.types.sses3.deserialize_xml(child_sses3)
    child_ssekms = el.find("SSE-KMS")
    if child_ssekms is not None:
        import aws_sdk_s3_control.types.ssekms

        out["ssekms"] = aws_sdk_s3_control.types.ssekms.deserialize_xml(child_ssekms)
    return out
