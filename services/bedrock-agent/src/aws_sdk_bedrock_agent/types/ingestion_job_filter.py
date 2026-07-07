"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IngestionJobFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.ingestion_job_filter_attribute
    import aws_sdk_bedrock_agent.types.ingestion_job_filter_operator
    import aws_sdk_bedrock_agent.types.ingestion_job_filter_values


class IngestionJobFilter(TypedDict, closed=True):
    attribute: "aws_sdk_bedrock_agent.types.ingestion_job_filter_attribute.IngestionJobFilterAttribute"
    """<p>The name of field or attribute to apply the filter.</p>"""
    operator: "aws_sdk_bedrock_agent.types.ingestion_job_filter_operator.IngestionJobFilterOperator"
    """<p>The operation to apply to the field or attribute.</p>"""
    values: "aws_sdk_bedrock_agent.types.ingestion_job_filter_values.IngestionJobFilterValues"
    """<p>A list of values that belong to the field or attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionJobFilter) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.ingestion_job_filter_attribute

    out["attribute"] = (
        aws_sdk_bedrock_agent.types.ingestion_job_filter_attribute.serialize_json(
            value["attribute"]
        )
    )
    import aws_sdk_bedrock_agent.types.ingestion_job_filter_operator

    out["operator"] = (
        aws_sdk_bedrock_agent.types.ingestion_job_filter_operator.serialize_json(
            value["operator"]
        )
    )
    import aws_sdk_bedrock_agent.types.ingestion_job_filter_values

    out["values"] = (
        aws_sdk_bedrock_agent.types.ingestion_job_filter_values.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> IngestionJobFilter:
    out: IngestionJobFilter = {}  # type: ignore[typeddict-item]
    if "attribute" in data:
        import aws_sdk_bedrock_agent.types.ingestion_job_filter_attribute

        out["attribute"] = (
            aws_sdk_bedrock_agent.types.ingestion_job_filter_attribute.deserialize_json(
                data["attribute"]
            )
        )
    else:
        raise DeserializationError("IngestionJobFilter.attribute required")
    if "operator" in data:
        import aws_sdk_bedrock_agent.types.ingestion_job_filter_operator

        out["operator"] = (
            aws_sdk_bedrock_agent.types.ingestion_job_filter_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        raise DeserializationError("IngestionJobFilter.operator required")
    if "values" in data:
        import aws_sdk_bedrock_agent.types.ingestion_job_filter_values

        out["values"] = (
            aws_sdk_bedrock_agent.types.ingestion_job_filter_values.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("IngestionJobFilter.values required")
    return out
