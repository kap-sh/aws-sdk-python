"""Generated from Smithy shape ``com.amazonaws.bedrockagent#NeptuneAnalyticsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.graph_arn
    import aws_sdk_bedrock_agent.types.neptune_analytics_field_mapping


class NeptuneAnalyticsConfiguration(TypedDict):
    graph_arn: "aws_sdk_bedrock_agent.types.graph_arn.GraphArn"
    """<p>The Amazon Resource Name (ARN) of the Neptune Analytics vector store.</p>"""
    field_mapping: "aws_sdk_bedrock_agent.types.neptune_analytics_field_mapping.NeptuneAnalyticsFieldMapping"
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NeptuneAnalyticsConfiguration) -> dict:
    out: dict = {}
    out["graphArn"] = value["graph_arn"]
    import aws_sdk_bedrock_agent.types.neptune_analytics_field_mapping

    out["fieldMapping"] = (
        aws_sdk_bedrock_agent.types.neptune_analytics_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    return out


def deserialize_json(data: dict) -> NeptuneAnalyticsConfiguration:
    out: NeptuneAnalyticsConfiguration = {}  # type: ignore[typeddict-item]
    if "graphArn" in data:
        out["graph_arn"] = data["graphArn"]
    else:
        raise DeserializationError("NeptuneAnalyticsConfiguration.graph_arn required")
    if "fieldMapping" in data:
        import aws_sdk_bedrock_agent.types.neptune_analytics_field_mapping

        out["field_mapping"] = (
            aws_sdk_bedrock_agent.types.neptune_analytics_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError(
            "NeptuneAnalyticsConfiguration.field_mapping required"
        )
    return out
