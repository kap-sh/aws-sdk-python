"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DocumentContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.content_data_source_type
    import aws_sdk_bedrock_agent.types.custom_content
    import aws_sdk_bedrock_agent.types.s3_content


class DocumentContent(TypedDict):
    data_source_type: (
        "aws_sdk_bedrock_agent.types.content_data_source_type.ContentDataSourceType"
    )
    """<p>The type of data source that is connected to the knowledge base to which to ingest this document.</p>"""
    custom: NotRequired["aws_sdk_bedrock_agent.types.custom_content.CustomContent"]
    """<p>Contains information about the content to ingest into a knowledge base connected to a custom data source.</p>"""
    s3: NotRequired["aws_sdk_bedrock_agent.types.s3_content.S3Content"]
    """<p>Contains information about the content to ingest into a knowledge base connected to an Amazon S3 data source</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentContent) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.content_data_source_type

    out["dataSourceType"] = (
        aws_sdk_bedrock_agent.types.content_data_source_type.serialize_json(
            value["data_source_type"]
        )
    )
    if "custom" in value:
        import aws_sdk_bedrock_agent.types.custom_content

        out["custom"] = aws_sdk_bedrock_agent.types.custom_content.serialize_json(
            value["custom"]
        )
    if "s3" in value:
        import aws_sdk_bedrock_agent.types.s3_content

        out["s3"] = aws_sdk_bedrock_agent.types.s3_content.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> DocumentContent:
    out: DocumentContent = {}  # type: ignore[typeddict-item]
    if "dataSourceType" in data:
        import aws_sdk_bedrock_agent.types.content_data_source_type

        out["data_source_type"] = (
            aws_sdk_bedrock_agent.types.content_data_source_type.deserialize_json(
                data["dataSourceType"]
            )
        )
    else:
        raise DeserializationError("DocumentContent.data_source_type required")
    if "custom" in data:
        import aws_sdk_bedrock_agent.types.custom_content

        out["custom"] = aws_sdk_bedrock_agent.types.custom_content.deserialize_json(
            data["custom"]
        )
    if "s3" in data:
        import aws_sdk_bedrock_agent.types.s3_content

        out["s3"] = aws_sdk_bedrock_agent.types.s3_content.deserialize_json(data["s3"])
    return out
