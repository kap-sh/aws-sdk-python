"""Generated from Smithy shape ``com.amazonaws.s3#MetadataTableEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.kms_key_arn
    import aws_sdk_s3.types.table_sse_algorithm


class MetadataTableEncryptionConfiguration(TypedDict):
    sse_algorithm: "aws_sdk_s3.types.table_sse_algorithm.TableSseAlgorithm"
    """<p> The encryption type specified for a metadata table. To specify server-side encryption with Key Management Service (KMS) keys (SSE-KMS), use the <code>aws:kms</code> value. To specify server-side encryption with Amazon S3 managed keys (SSE-S3), use the <code>AES256</code> value. </p>"""
    kms_key_arn: NotRequired["aws_sdk_s3.types.kms_key_arn.KmsKeyArn"]
    """<p> If server-side encryption with Key Management Service (KMS) keys (SSE-KMS) is specified, you must also specify the KMS key Amazon Resource Name (ARN). You must specify a customer-managed KMS key that's located in the same Region as the general purpose bucket that corresponds to the metadata table configuration. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: MetadataTableEncryptionConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.table_sse_algorithm

    aws_sdk_s3.types.table_sse_algorithm.serialize_xml(
        value["sse_algorithm"], el, "SseAlgorithm"
    )
    if "kms_key_arn" in value:
        SubElement(el, "KmsKeyArn").text = str(value["kms_key_arn"])


def deserialize_xml(el: Element) -> MetadataTableEncryptionConfiguration:
    out: MetadataTableEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    child_sse_algorithm = el.find("SseAlgorithm")
    if child_sse_algorithm is not None:
        import aws_sdk_s3.types.table_sse_algorithm

        out["sse_algorithm"] = aws_sdk_s3.types.table_sse_algorithm.deserialize_xml(
            child_sse_algorithm
        )
    else:
        raise DeserializationError(
            "MetadataTableEncryptionConfiguration.sse_algorithm required"
        )
    child_kms_key_arn = el.find("KmsKeyArn")
    if child_kms_key_arn is not None:
        out["kms_key_arn"] = str(child_kms_key_arn.text or "")
    return out
