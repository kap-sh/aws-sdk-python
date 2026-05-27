"""Generated from Smithy shape ``com.amazonaws.s3#JournalTableConfigurationResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_s3.errors import DeserializationError
from aws_sdk_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3.types.error_details
    import aws_sdk_s3.types.metadata_table_status
    import aws_sdk_s3.types.record_expiration
    import aws_sdk_s3.types.s3_tables_arn
    import aws_sdk_s3.types.s3_tables_name


class JournalTableConfigurationResult(TypedDict):
    table_status: "aws_sdk_s3.types.metadata_table_status.MetadataTableStatus"
    """<p> The status of the journal table. The status values are: </p> <ul> <li> <p> <code>CREATING</code> - The journal table is in the process of being created in the specified table bucket.</p> </li> <li> <p> <code>ACTIVE</code> - The journal table has been created successfully, and records are being delivered to the table. </p> </li> <li> <p> <code>FAILED</code> - Amazon S3 is unable to create the journal table, or Amazon S3 is unable to deliver records.</p> </li> </ul>"""
    error: NotRequired["aws_sdk_s3.types.error_details.ErrorDetails"]
    table_name: "aws_sdk_s3.types.s3_tables_name.S3TablesName"
    """<p> The name of the journal table. </p>"""
    table_arn: NotRequired["aws_sdk_s3.types.s3_tables_arn.S3TablesArn"]
    """<p> The Amazon Resource Name (ARN) for the journal table. </p>"""
    record_expiration: "aws_sdk_s3.types.record_expiration.RecordExpiration"
    """<p> The journal table record expiration settings for the journal table. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: JournalTableConfigurationResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "TableStatus").text = str(value["table_status"])
    if "error" in value:
        import aws_sdk_s3.types.error_details

        aws_sdk_s3.types.error_details.serialize_xml(value["error"], el, "Error")
    SubElement(el, "TableName").text = str(value["table_name"])
    if "table_arn" in value:
        SubElement(el, "TableArn").text = str(value["table_arn"])
    import aws_sdk_s3.types.record_expiration

    aws_sdk_s3.types.record_expiration.serialize_xml(
        value["record_expiration"], el, "RecordExpiration"
    )


def deserialize_xml(el: Element) -> JournalTableConfigurationResult:
    out: JournalTableConfigurationResult = {}  # type: ignore[typeddict-item]
    child_table_status = el.find("TableStatus")
    if child_table_status is not None:
        out["table_status"] = str(child_table_status.text or "")
    else:
        raise DeserializationError(
            "JournalTableConfigurationResult.table_status required"
        )
    child_error = el.find("Error")
    if child_error is not None:
        import aws_sdk_s3.types.error_details

        out["error"] = aws_sdk_s3.types.error_details.deserialize_xml(child_error)
    child_table_name = el.find("TableName")
    if child_table_name is not None:
        out["table_name"] = str(child_table_name.text or "")
    else:
        raise DeserializationError(
            "JournalTableConfigurationResult.table_name required"
        )
    child_table_arn = el.find("TableArn")
    if child_table_arn is not None:
        out["table_arn"] = str(child_table_arn.text or "")
    child_record_expiration = el.find("RecordExpiration")
    if child_record_expiration is not None:
        import aws_sdk_s3.types.record_expiration

        out["record_expiration"] = aws_sdk_s3.types.record_expiration.deserialize_xml(
            child_record_expiration
        )
    else:
        raise DeserializationError(
            "JournalTableConfigurationResult.record_expiration required"
        )
    return out
