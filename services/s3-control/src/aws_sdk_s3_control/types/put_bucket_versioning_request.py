"""Generated from Smithy shape ``com.amazonaws.s3control#PutBucketVersioningRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement
from aws_sdk_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.account_id
    import aws_sdk_s3_control.types.bucket_name
    import aws_sdk_s3_control.types.mfa
    import aws_sdk_s3_control.types.versioning_configuration


class PutBucketVersioningRequest(TypedDict):
    account_id: "aws_sdk_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the S3 on Outposts bucket.</p>"""
    bucket: "aws_sdk_s3_control.types.bucket_name.BucketName"
    """<p>The S3 on Outposts bucket to set the versioning state for.</p>"""
    mfa: NotRequired["aws_sdk_s3_control.types.mfa.MFA"]
    """<p>The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device.</p>"""
    versioning_configuration: (
        "aws_sdk_s3_control.types.versioning_configuration.VersioningConfiguration"
    )
    """<p>The root-level tag for the <code>VersioningConfiguration</code> parameters.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutBucketVersioningRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3_control.types.versioning_configuration

    aws_sdk_s3_control.types.versioning_configuration.serialize_xml(
        value["versioning_configuration"], el, "VersioningConfiguration"
    )


def deserialize_xml(el: Element) -> PutBucketVersioningRequest:
    out: PutBucketVersioningRequest = {}  # type: ignore[typeddict-item]
    child_versioning_configuration = el.find("VersioningConfiguration")
    if child_versioning_configuration is not None:
        import aws_sdk_s3_control.types.versioning_configuration

        out["versioning_configuration"] = (
            aws_sdk_s3_control.types.versioning_configuration.deserialize_xml(
                child_versioning_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketVersioningRequest.versioning_configuration required"
        )
    return out
