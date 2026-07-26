"""Generated from Smithy shape ``com.amazonaws.s3control#SSEKMSFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.boolean
    import capo_s3_control.types.non_empty_kms_key_arn_string


class SSEKMSFilter(TypedDict, closed=True):
    kms_key_arn: NotRequired[
        "capo_s3_control.types.non_empty_kms_key_arn_string.NonEmptyKmsKeyArnString"
    ]
    """<p>The Amazon Resource Name (ARN) of the customer managed KMS key to use for the filter to return objects that are encrypted by the specified key. For best performance, use keys in the same Region as the S3 Batch Operations job.</p>"""
    bucket_key_enabled: NotRequired["capo_s3_control.types.boolean.Boolean"]
    """<p>Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with server-side encryption using Amazon Web Services Key Management Service (Amazon Web Services KMS) keys (SSE-KMS). If specified, will filter SSE-KMS encrypted objects by S3 Bucket Key status.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: SSEKMSFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "kms_key_arn" in value:
        SubElement(el, "KmsKeyArn").text = str(value["kms_key_arn"])
    if "bucket_key_enabled" in value:
        SubElement(el, "BucketKeyEnabled").text = (
            "true" if value["bucket_key_enabled"] else "false"
        )


def deserialize_xml(el: Element) -> SSEKMSFilter:
    out: SSEKMSFilter = {}  # type: ignore[typeddict-item]
    child_kms_key_arn = el.find("KmsKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    child_bucket_key_enabled = el.find("BucketKeyEnabled")
    if child_bucket_key_enabled is not None:
        out["bucket_key_enabled"] = (
            child_bucket_key_enabled.text or ""
        ).lower() == "true"
    return out
