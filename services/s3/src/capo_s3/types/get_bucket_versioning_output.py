"""Generated from Smithy shape ``com.amazonaws.s3#GetBucketVersioningOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.bucket_versioning_status
    import capo_s3.types.mfa_delete_status


class GetBucketVersioningOutput(TypedDict, closed=True):
    status: NotRequired["capo_s3.types.bucket_versioning_status.BucketVersioningStatus"]
    """<p>The versioning state of the bucket.</p>"""
    mfa_delete: NotRequired["capo_s3.types.mfa_delete_status.MFADeleteStatus"]
    """<p>Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketVersioningOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "status" in value:
        import capo_s3.types.bucket_versioning_status

        capo_s3.types.bucket_versioning_status.serialize_xml(
            value["status"], el, "Status"
        )
    if "mfa_delete" in value:
        import capo_s3.types.mfa_delete_status

        capo_s3.types.mfa_delete_status.serialize_xml(
            value["mfa_delete"], el, "MfaDelete"
        )


def deserialize_xml(el: Element) -> GetBucketVersioningOutput:
    out: GetBucketVersioningOutput = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.bucket_versioning_status

        out["status"] = capo_s3.types.bucket_versioning_status.deserialize_xml(
            child_status
        )
    child_mfa_delete = el.find("MfaDelete")
    if child_mfa_delete is not None:
        import capo_s3.types.mfa_delete_status

        out["mfa_delete"] = capo_s3.types.mfa_delete_status.deserialize_xml(
            child_mfa_delete
        )
    return out
