"""Generated from Smithy shape ``com.amazonaws.s3control#GeneratedManifestEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.ssekms_encryption
    import capo_s3_control.types.sses3_encryption


class GeneratedManifestEncryption(TypedDict, closed=True):
    sses3: NotRequired["capo_s3_control.types.sses3_encryption.SSES3Encryption"]
    """<p>Specifies the use of SSE-S3 to encrypt generated manifest objects.</p>"""
    ssekms: NotRequired["capo_s3_control.types.ssekms_encryption.SSEKMSEncryption"]
    """<p>Configuration details on how SSE-KMS is used to encrypt generated manifest objects.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GeneratedManifestEncryption, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "sses3" in value:
        import capo_s3_control.types.sses3_encryption

        capo_s3_control.types.sses3_encryption.serialize_xml(
            value["sses3"], el, "SSE-S3"
        )
    if "ssekms" in value:
        import capo_s3_control.types.ssekms_encryption

        capo_s3_control.types.ssekms_encryption.serialize_xml(
            value["ssekms"], el, "SSE-KMS"
        )


def deserialize_xml(el: Element) -> GeneratedManifestEncryption:
    out: GeneratedManifestEncryption = {}  # type: ignore[typeddict-item]
    child_sses3 = el.find("SSE-S3")
    if child_sses3 is not None:
        import capo_s3_control.types.sses3_encryption

        out["sses3"] = capo_s3_control.types.sses3_encryption.deserialize_xml(
            child_sses3
        )
    child_ssekms = el.find("SSE-KMS")
    if child_ssekms is not None:
        import capo_s3_control.types.ssekms_encryption

        out["ssekms"] = capo_s3_control.types.ssekms_encryption.deserialize_xml(
            child_ssekms
        )
    return out
