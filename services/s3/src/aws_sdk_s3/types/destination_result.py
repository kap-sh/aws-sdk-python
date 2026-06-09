"""Generated from Smithy shape ``com.amazonaws.s3#DestinationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.s3_tables_bucket_arn
    import aws_sdk_s3.types.s3_tables_bucket_type
    import aws_sdk_s3.types.s3_tables_namespace


class DestinationResult(TypedDict):
    table_bucket_type: NotRequired[
        "aws_sdk_s3.types.s3_tables_bucket_type.S3TablesBucketType"
    ]
    """<p> The type of the table bucket where the metadata configuration is stored. The <code>aws</code> value indicates an Amazon Web Services managed table bucket, and the <code>customer</code> value indicates a customer-managed table bucket. V2 metadata configurations are stored in Amazon Web Services managed table buckets, and V1 metadata configurations are stored in customer-managed table buckets. </p>"""
    table_bucket_arn: NotRequired[
        "aws_sdk_s3.types.s3_tables_bucket_arn.S3TablesBucketArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the table bucket where the metadata configuration is stored. </p>"""
    table_namespace: NotRequired[
        "aws_sdk_s3.types.s3_tables_namespace.S3TablesNamespace"
    ]
    """<p> The namespace in the table bucket where the metadata tables for a metadata configuration are stored. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: DestinationResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "table_bucket_type" in value:
        import aws_sdk_s3.types.s3_tables_bucket_type

        aws_sdk_s3.types.s3_tables_bucket_type.serialize_xml(
            value["table_bucket_type"], el, "TableBucketType"
        )
    if "table_bucket_arn" in value:
        SubElement(el, "TableBucketArn").text = str(value["table_bucket_arn"])
    if "table_namespace" in value:
        SubElement(el, "TableNamespace").text = str(value["table_namespace"])


def deserialize_xml(el: Element) -> DestinationResult:
    out: DestinationResult = {}  # type: ignore[typeddict-item]
    child_table_bucket_type = el.find("TableBucketType")
    if child_table_bucket_type is not None:
        import aws_sdk_s3.types.s3_tables_bucket_type

        out["table_bucket_type"] = (
            aws_sdk_s3.types.s3_tables_bucket_type.deserialize_xml(
                child_table_bucket_type
            )
        )
    child_table_bucket_arn = el.find("TableBucketArn")
    if child_table_bucket_arn is not None:
        out["table_bucket_arn"] = str(child_table_bucket_arn.text or "")
    child_table_namespace = el.find("TableNamespace")
    if child_table_namespace is not None:
        out["table_namespace"] = str(child_table_namespace.text or "")
    return out
