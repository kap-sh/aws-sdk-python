"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id
    import aws_sdk_qbusiness.types.description
    import aws_sdk_qbusiness.types.document_attribute_configurations
    import aws_sdk_qbusiness.types.error_detail
    import aws_sdk_qbusiness.types.index_arn
    import aws_sdk_qbusiness.types.index_capacity_configuration
    import aws_sdk_qbusiness.types.index_id
    import aws_sdk_qbusiness.types.index_name
    import aws_sdk_qbusiness.types.index_statistics
    import aws_sdk_qbusiness.types.index_status
    import aws_sdk_qbusiness.types.index_type
    import aws_sdk_qbusiness.types.timestamp


class GetIndexResponse(TypedDict, closed=True):
    application_id: NotRequired["aws_sdk_qbusiness.types.application_id.ApplicationId"]
    """<p>The identifier of the Amazon Q Business application associated with the index.</p>"""
    index_id: NotRequired["aws_sdk_qbusiness.types.index_id.IndexId"]
    """<p>The identifier of the Amazon Q Business index.</p>"""
    display_name: NotRequired["aws_sdk_qbusiness.types.index_name.IndexName"]
    """<p>The name of the Amazon Q Business index.</p>"""
    index_arn: NotRequired["aws_sdk_qbusiness.types.index_arn.IndexArn"]
    """<p> The Amazon Resource Name (ARN) of the Amazon Q Business index. </p>"""
    status: NotRequired["aws_sdk_qbusiness.types.index_status.IndexStatus"]
    """<p>The current status of the index. When the value is <code>ACTIVE</code>, the index is ready for use. If the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.index_type.IndexType"]
    """<p>The type of index attached to your Amazon Q Business application.</p>"""
    description: NotRequired["aws_sdk_qbusiness.types.description.Description"]
    """<p>The description for the Amazon Q Business index.</p>"""
    created_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business index was created.</p>"""
    updated_at: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the Amazon Q Business index was last updated.</p>"""
    capacity_configuration: NotRequired[
        "aws_sdk_qbusiness.types.index_capacity_configuration.IndexCapacityConfiguration"
    ]
    """<p>The storage capacity units chosen for your Amazon Q Business index.</p>"""
    document_attribute_configurations: NotRequired[
        "aws_sdk_qbusiness.types.document_attribute_configurations.DocumentAttributeConfigurations"
    ]
    r"""<p>Configuration information for document attributes or metadata. Document metadata are fields associated with your documents. For example, the company department name associated with each document. For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes-types.html#doc-attributes\">Understanding document attributes</a>.</p>"""
    error: NotRequired["aws_sdk_qbusiness.types.error_detail.ErrorDetail"]
    """<p>When the <code>Status</code> field value is <code>FAILED</code>, the <code>ErrorMessage</code> field contains a message that explains why.</p>"""
    index_statistics: NotRequired[
        "aws_sdk_qbusiness.types.index_statistics.IndexStatistics"
    ]
    """<p>Provides information about the number of documents indexed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexResponse) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "index_id" in value:
        out["indexId"] = value["index_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    if "status" in value:
        import aws_sdk_qbusiness.types.index_status

        out["status"] = aws_sdk_qbusiness.types.index_status.serialize_json(
            value["status"]
        )
    if "type" in value:
        import aws_sdk_qbusiness.types.index_type

        out["type"] = aws_sdk_qbusiness.types.index_type.serialize_json(value["type"])
    if "description" in value:
        out["description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["createdAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["updatedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "capacity_configuration" in value:
        import aws_sdk_qbusiness.types.index_capacity_configuration

        out["capacityConfiguration"] = (
            aws_sdk_qbusiness.types.index_capacity_configuration.serialize_json(
                value["capacity_configuration"]
            )
        )
    if "document_attribute_configurations" in value:
        import aws_sdk_qbusiness.types.document_attribute_configurations

        out["documentAttributeConfigurations"] = (
            aws_sdk_qbusiness.types.document_attribute_configurations.serialize_json(
                value["document_attribute_configurations"]
            )
        )
    if "error" in value:
        import aws_sdk_qbusiness.types.error_detail

        out["error"] = aws_sdk_qbusiness.types.error_detail.serialize_json(
            value["error"]
        )
    if "index_statistics" in value:
        import aws_sdk_qbusiness.types.index_statistics

        out["indexStatistics"] = (
            aws_sdk_qbusiness.types.index_statistics.serialize_json(
                value["index_statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetIndexResponse:
    out: GetIndexResponse = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "indexId" in data:
        out["index_id"] = data["indexId"]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    if "status" in data:
        import aws_sdk_qbusiness.types.index_status

        out["status"] = aws_sdk_qbusiness.types.index_status.deserialize_json(
            data["status"]
        )
    if "type" in data:
        import aws_sdk_qbusiness.types.index_type

        out["type"] = aws_sdk_qbusiness.types.index_type.deserialize_json(data["type"])
    if "description" in data:
        out["description"] = data["description"]
    if "createdAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["created_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if "updatedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["updated_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if "capacityConfiguration" in data:
        import aws_sdk_qbusiness.types.index_capacity_configuration

        out["capacity_configuration"] = (
            aws_sdk_qbusiness.types.index_capacity_configuration.deserialize_json(
                data["capacityConfiguration"]
            )
        )
    if "documentAttributeConfigurations" in data:
        import aws_sdk_qbusiness.types.document_attribute_configurations

        out["document_attribute_configurations"] = (
            aws_sdk_qbusiness.types.document_attribute_configurations.deserialize_json(
                data["documentAttributeConfigurations"]
            )
        )
    if "error" in data:
        import aws_sdk_qbusiness.types.error_detail

        out["error"] = aws_sdk_qbusiness.types.error_detail.deserialize_json(
            data["error"]
        )
    if "indexStatistics" in data:
        import aws_sdk_qbusiness.types.index_statistics

        out["index_statistics"] = (
            aws_sdk_qbusiness.types.index_statistics.deserialize_json(
                data["indexStatistics"]
            )
        )
    return out
