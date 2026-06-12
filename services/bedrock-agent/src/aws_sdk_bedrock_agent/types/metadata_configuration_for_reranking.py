"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataConfigurationForReranking``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.reranking_metadata_selection_mode
    import aws_sdk_bedrock_agent.types.reranking_metadata_selective_mode_configuration


class MetadataConfigurationForReranking(TypedDict):
    selection_mode: "aws_sdk_bedrock_agent.types.reranking_metadata_selection_mode.RerankingMetadataSelectionMode"
    """<p>The mode for selecting metadata fields for reranking.</p>"""
    selective_mode_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.reranking_metadata_selective_mode_configuration.RerankingMetadataSelectiveModeConfiguration"
    ]
    """<p>The configuration for selective metadata field inclusion or exclusion during reranking.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfigurationForReranking) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.reranking_metadata_selection_mode

    out["selectionMode"] = (
        aws_sdk_bedrock_agent.types.reranking_metadata_selection_mode.serialize_json(
            value["selection_mode"]
        )
    )
    if "selective_mode_configuration" in value:
        import aws_sdk_bedrock_agent.types.reranking_metadata_selective_mode_configuration

        out["selectiveModeConfiguration"] = (
            aws_sdk_bedrock_agent.types.reranking_metadata_selective_mode_configuration.serialize_json(
                value["selective_mode_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataConfigurationForReranking:
    out: MetadataConfigurationForReranking = {}  # type: ignore[typeddict-item]
    if "selectionMode" in data:
        import aws_sdk_bedrock_agent.types.reranking_metadata_selection_mode

        out["selection_mode"] = (
            aws_sdk_bedrock_agent.types.reranking_metadata_selection_mode.deserialize_json(
                data["selectionMode"]
            )
        )
    else:
        raise DeserializationError(
            "MetadataConfigurationForReranking.selection_mode required"
        )
    if "selectiveModeConfiguration" in data:
        import aws_sdk_bedrock_agent.types.reranking_metadata_selective_mode_configuration

        out["selective_mode_configuration"] = (
            aws_sdk_bedrock_agent.types.reranking_metadata_selective_mode_configuration.deserialize_json(
                data["selectiveModeConfiguration"]
            )
        )
    return out
