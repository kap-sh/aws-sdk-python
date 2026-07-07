"""Generated from Smithy shape ``com.amazonaws.s3control#VersioningConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.bucket_versioning_status
    import aws_sdk_s3_control.types.mfa_delete


class VersioningConfiguration(TypedDict, closed=True):
    mfa_delete: NotRequired["aws_sdk_s3_control.types.mfa_delete.MFADelete"]
    """<p>Specifies whether MFA delete is enabled or disabled in the bucket versioning configuration for the S3 on Outposts bucket.</p>"""
    status: NotRequired[
        "aws_sdk_s3_control.types.bucket_versioning_status.BucketVersioningStatus"
    ]
    """<p>Sets the versioning state of the S3 on Outposts bucket.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: VersioningConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "mfa_delete" in value:
        import aws_sdk_s3_control.types.mfa_delete

        aws_sdk_s3_control.types.mfa_delete.serialize_xml(
            value["mfa_delete"], el, "MfaDelete"
        )
    if "status" in value:
        import aws_sdk_s3_control.types.bucket_versioning_status

        aws_sdk_s3_control.types.bucket_versioning_status.serialize_xml(
            value["status"], el, "Status"
        )


def deserialize_xml(el: Element) -> VersioningConfiguration:
    out: VersioningConfiguration = {}  # type: ignore[typeddict-item]
    child_mfa_delete = el.find("MfaDelete")
    if child_mfa_delete is not None:
        import aws_sdk_s3_control.types.mfa_delete

        out["mfa_delete"] = aws_sdk_s3_control.types.mfa_delete.deserialize_xml(
            child_mfa_delete
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_s3_control.types.bucket_versioning_status

        out["status"] = (
            aws_sdk_s3_control.types.bucket_versioning_status.deserialize_xml(
                child_status
            )
        )
    return out
