"""Generated from Smithy shape ``com.amazonaws.s3control#GetBucketVersioningResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.bucket_versioning_status
    import aws_sdk_s3_control.types.mfa_delete_status


class GetBucketVersioningResult(TypedDict):
    status: NotRequired[
        "aws_sdk_s3_control.types.bucket_versioning_status.BucketVersioningStatus"
    ]
    """<p>The versioning state of the S3 on Outposts bucket.</p>"""
    mfa_delete: NotRequired[
        "aws_sdk_s3_control.types.mfa_delete_status.MFADeleteStatus"
    ]
    """<p>Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is returned only if the bucket has been configured with MFA delete. If MFA delete has never been configured for the bucket, this element is not returned.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetBucketVersioningResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "status" in value:
        import aws_sdk_s3_control.types.bucket_versioning_status

        aws_sdk_s3_control.types.bucket_versioning_status.serialize_xml(
            value["status"], el, "Status"
        )
    if "mfa_delete" in value:
        import aws_sdk_s3_control.types.mfa_delete_status

        aws_sdk_s3_control.types.mfa_delete_status.serialize_xml(
            value["mfa_delete"], el, "MfaDelete"
        )


def deserialize_xml(el: Element) -> GetBucketVersioningResult:
    out: GetBucketVersioningResult = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3_control.types.bucket_versioning_status

        out["status"] = (
            aws_sdk_s3_control.types.bucket_versioning_status.deserialize_xml(
                child_status
            )
        )
    child_mfa_delete = el.find("MfaDelete")
    if child_mfa_delete is not None:
        import aws_sdk_s3_control.types.mfa_delete_status

        out["mfa_delete"] = aws_sdk_s3_control.types.mfa_delete_status.deserialize_xml(
            child_mfa_delete
        )
    return out
