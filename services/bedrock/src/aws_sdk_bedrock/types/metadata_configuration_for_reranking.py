"""Generated from Smithy shape ``com.amazonaws.bedrock#MetadataConfigurationForReranking``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.reranking_metadata_selection_mode
    import aws_sdk_bedrock.types.reranking_metadata_selective_mode_configuration


class MetadataConfigurationForReranking(TypedDict):
    selection_mode: "aws_sdk_bedrock.types.reranking_metadata_selection_mode.RerankingMetadataSelectionMode"
    """<p>The mode for selecting which metadata fields to include in the reranking process. Valid values are ALL (use all available metadata fields) or SELECTIVE (use only specified fields).</p>"""
    selective_mode_configuration: NotRequired[
        "aws_sdk_bedrock.types.reranking_metadata_selective_mode_configuration.RerankingMetadataSelectiveModeConfiguration"
    ]
    """<p>Configuration for selective mode, which allows you to explicitly include or exclude specific metadata fields during reranking. This is only used when selectionMode is set to SELECTIVE.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfigurationForReranking) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.reranking_metadata_selection_mode

    out["selectionMode"] = (
        aws_sdk_bedrock.types.reranking_metadata_selection_mode.serialize_json(
            value["selection_mode"]
        )
    )
    if "selective_mode_configuration" in value:
        import aws_sdk_bedrock.types.reranking_metadata_selective_mode_configuration

        out["selectiveModeConfiguration"] = (
            aws_sdk_bedrock.types.reranking_metadata_selective_mode_configuration.serialize_json(
                value["selective_mode_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataConfigurationForReranking:
    out: MetadataConfigurationForReranking = {}  # type: ignore[typeddict-item]
    if "selectionMode" in data:
        import aws_sdk_bedrock.types.reranking_metadata_selection_mode

        out["selection_mode"] = (
            aws_sdk_bedrock.types.reranking_metadata_selection_mode.deserialize_json(
                data["selectionMode"]
            )
        )
    else:
        raise DeserializationError(
            "MetadataConfigurationForReranking.selection_mode required"
        )
    if "selectiveModeConfiguration" in data:
        import aws_sdk_bedrock.types.reranking_metadata_selective_mode_configuration

        out["selective_mode_configuration"] = (
            aws_sdk_bedrock.types.reranking_metadata_selective_mode_configuration.deserialize_json(
                data["selectiveModeConfiguration"]
            )
        )
    return out
