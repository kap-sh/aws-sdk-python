"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievalResultLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_confluence_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_custom_document_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_kendra_document_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_location_type
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_s3_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_salesforce_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_share_point_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_sql_location
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_web_location


class RetrievalResultLocation(TypedDict, closed=True):
    type: "aws_sdk_bedrock_agent_runtime.types.retrieval_result_location_type.RetrievalResultLocationType"
    """<p>The type of data source location.</p>"""
    s3_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_s3_location.RetrievalResultS3Location"
    ]
    """<p>The S3 data source location.</p>"""
    web_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_web_location.RetrievalResultWebLocation"
    ]
    """<p>The web URL/URLs data source location.</p>"""
    confluence_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_confluence_location.RetrievalResultConfluenceLocation"
    ]
    """<p>The Confluence data source location.</p>"""
    salesforce_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_salesforce_location.RetrievalResultSalesforceLocation"
    ]
    """<p>The Salesforce data source location.</p>"""
    share_point_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_share_point_location.RetrievalResultSharePointLocation"
    ]
    """<p>The SharePoint data source location.</p>"""
    custom_document_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_custom_document_location.RetrievalResultCustomDocumentLocation"
    ]
    """<p>Specifies the location of a document in a custom data source.</p>"""
    kendra_document_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_kendra_document_location.RetrievalResultKendraDocumentLocation"
    ]
    """<p>The location of a document in Amazon Kendra.</p>"""
    sql_location: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.retrieval_result_sql_location.RetrievalResultSqlLocation"
    ]
    """<p>Specifies information about the SQL query used to retrieve the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrievalResultLocation) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent_runtime.types.retrieval_result_location_type

    out["type"] = (
        aws_sdk_bedrock_agent_runtime.types.retrieval_result_location_type.serialize_json(
            value["type"]
        )
    )
    if "s3_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_s3_location

        out["s3Location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_s3_location.serialize_json(
                value["s3_location"]
            )
        )
    if "web_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_web_location

        out["webLocation"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_web_location.serialize_json(
                value["web_location"]
            )
        )
    if "confluence_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_confluence_location

        out["confluenceLocation"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_confluence_location.serialize_json(
                value["confluence_location"]
            )
        )
    if "salesforce_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_salesforce_location

        out["salesforceLocation"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_salesforce_location.serialize_json(
                value["salesforce_location"]
            )
        )
    if "share_point_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_share_point_location

        out["sharePointLocation"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_share_point_location.serialize_json(
                value["share_point_location"]
            )
        )
    if "custom_document_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_custom_document_location

        out["customDocumentLocation"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_custom_document_location.serialize_json(
                value["custom_document_location"]
            )
        )
    if "kendra_document_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_kendra_document_location

        out["kendraDocumentLocation"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_kendra_document_location.serialize_json(
                value["kendra_document_location"]
            )
        )
    if "sql_location" in value:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_sql_location

        out["sqlLocation"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_sql_location.serialize_json(
                value["sql_location"]
            )
        )
    return out


def deserialize_json(data: dict) -> RetrievalResultLocation:
    out: RetrievalResultLocation = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_location_type

        out["type"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_location_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("RetrievalResultLocation.type required")
    if "s3Location" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_s3_location

        out["s3_location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_s3_location.deserialize_json(
                data["s3Location"]
            )
        )
    if "webLocation" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_web_location

        out["web_location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_web_location.deserialize_json(
                data["webLocation"]
            )
        )
    if "confluenceLocation" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_confluence_location

        out["confluence_location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_confluence_location.deserialize_json(
                data["confluenceLocation"]
            )
        )
    if "salesforceLocation" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_salesforce_location

        out["salesforce_location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_salesforce_location.deserialize_json(
                data["salesforceLocation"]
            )
        )
    if "sharePointLocation" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_share_point_location

        out["share_point_location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_share_point_location.deserialize_json(
                data["sharePointLocation"]
            )
        )
    if "customDocumentLocation" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_custom_document_location

        out["custom_document_location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_custom_document_location.deserialize_json(
                data["customDocumentLocation"]
            )
        )
    if "kendraDocumentLocation" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_kendra_document_location

        out["kendra_document_location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_kendra_document_location.deserialize_json(
                data["kendraDocumentLocation"]
            )
        )
    if "sqlLocation" in data:
        import aws_sdk_bedrock_agent_runtime.types.retrieval_result_sql_location

        out["sql_location"] = (
            aws_sdk_bedrock_agent_runtime.types.retrieval_result_sql_location.deserialize_json(
                data["sqlLocation"]
            )
        )
    return out
