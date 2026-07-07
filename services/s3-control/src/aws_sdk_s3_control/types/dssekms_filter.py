"""Generated from Smithy shape ``com.amazonaws.s3control#DSSEKMSFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.non_empty_kms_key_arn_string


class DSSEKMSFilter(TypedDict, closed=True):
    kms_key_arn: NotRequired[
        "aws_sdk_s3_control.types.non_empty_kms_key_arn_string.NonEmptyKmsKeyArnString"
    ]
    """<p>The Amazon Resource Name (ARN) of the customer managed KMS key to use for the filter to return objects that are encrypted by the specified key. For best performance, use keys in the same Region as the S3 Batch Operations job.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: DSSEKMSFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "kms_key_arn" in value:
        SubElement(el, "KmsKeyArn").text = str(value["kms_key_arn"])


def deserialize_xml(el: Element) -> DSSEKMSFilter:
    out: DSSEKMSFilter = {}  # type: ignore[typeddict-item]
    child_kms_key_arn = el.find("KmsKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    return out
