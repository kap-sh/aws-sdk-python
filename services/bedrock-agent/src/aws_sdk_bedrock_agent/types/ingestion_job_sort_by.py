"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobSortBy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.ingestion_job_sort_by_attribute
    import aws_sdk_bedrock_agent.types.sort_order


class IngestionJobSortBy(TypedDict, closed=True):
    attribute: "aws_sdk_bedrock_agent.types.ingestion_job_sort_by_attribute.IngestionJobSortByAttribute"
    """<p>The name of field or attribute to apply sorting of data.</p>"""
    order: "aws_sdk_bedrock_agent.types.sort_order.SortOrder"
    """<p>The order for sorting the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobSortBy) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.ingestion_job_sort_by_attribute

    out["attribute"] = (
        aws_sdk_bedrock_agent.types.ingestion_job_sort_by_attribute.serialize_json(
            value["attribute"]
        )
    )
    import aws_sdk_bedrock_agent.types.sort_order

    out["order"] = aws_sdk_bedrock_agent.types.sort_order.serialize_json(value["order"])
    return out


def deserialize_json(data: dict) -> IngestionJobSortBy:
    out: IngestionJobSortBy = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import aws_sdk_bedrock_agent.types.ingestion_job_sort_by_attribute

        out["attribute"] = (
            aws_sdk_bedrock_agent.types.ingestion_job_sort_by_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("IngestionJobSortBy.attribute required")
    if "order" in data:
        import aws_sdk_bedrock_agent.types.sort_order

        out["order"] = aws_sdk_bedrock_agent.types.sort_order.deserialize_json(
            data["order"]
        )
    else:
        raise DeserializationError("IngestionJobSortBy.order required")
    return out
